import os
import time
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request


load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
REDIS_DECODE_RESPONSES = os.getenv('REDIS_DECODE_RESPONSES')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(host=REDIS_HOST,
                              port=REDIS_PORT,
                              password=REDIS_PASSWORD,
                              decode_responses=REDIS_DECODE_RESPONSES
                              )


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Meta:
        database = redis


@app.get('/orders')
def all():
    return [format(pk) for pk in Order.all_pks()]


def format(pk: str):
    order = Order.get(pk)

    return {
        'pk': order.pk,
        'product_id': order.product_id,
        'price': order.price,
        'fee': order.fee,
        'quantity': order.quantity,
        'status': order.status
    }


@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)


@app.post('/orders')
async def create(request: Request, background_tasks: BackgroundTasks):  # id, quantity
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
            product_id=body['id'],
            price=product['price'],
            fee=0.2 * product['price'],
            total=1.2 * product['price'],
            quantity=body['quantity'],
            status='pending'
    )

    order.save()

    background_tasks.add_task(order_completed, order)

    return order


def order_completed(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save()
    redis.xadd('order_completed', order.dict(), '*')  # * = id parameter of current event, auto generated


@app.delete('/orders/{pk}')
def delete(pk: str):
    return Order.delete(pk)

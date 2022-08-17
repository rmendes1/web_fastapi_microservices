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

redis2 = get_redis_connection(host=REDIS_HOST,
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
        database = redis2


@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)


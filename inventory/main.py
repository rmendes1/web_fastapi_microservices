import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

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


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

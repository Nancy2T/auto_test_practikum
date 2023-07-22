import requests

from urllib.parse import urljoin

from settings.configuration import SERVICE_URL, CREATE_ORDER_PATH, GET_ORDER_PATH
from tests.utils.create_order_data import create_order_data


def post_create_order() -> str:
    """метод создания заказа"""
    response = requests.post(url=urljoin(SERVICE_URL, CREATE_ORDER_PATH), json=create_order_data())
    response.raise_for_status()
    return response.json()['track']


def get_status_order_data(track_id: str) -> int:
    """метод получения заказа по номеру"""
    response = requests.get(url=urljoin(SERVICE_URL, GET_ORDER_PATH), params={'t': track_id})
    return response.status_code


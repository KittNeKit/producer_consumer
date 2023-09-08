from datetime import datetime

import requests
from django.contrib.auth.models import User

from producer_consumer.settings import TELEGRAM_TOKEN
from service.models import Order, Employee


def send_notification(message: str, chat_id: int) -> None:
    """
    Sends a message to user
    """
    if chat_id:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.get(url, params={"chat_id": chat_id, "text": message})


def send_delete_order_text(order: Order, employee: Employee | User) -> None:
    """Sends a message while deleting order with detailed info"""
    message = (
        f"Задача №{order.pk}-{order.task_id} під назвою {order.name}"
        f" була опрацьована {employee.first_name} {employee.position}"
        f" у {datetime.now()}🟢"
    )
    send_notification(message, employee.telegram_id)

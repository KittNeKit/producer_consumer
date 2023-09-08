import random

from celery import shared_task
from django.db.models import Max

from service.models import Order, Employee


@shared_task
def create_order():
    max_id = Employee.objects.all().aggregate(max_id=Max("id"))["max_id"]
    while True:
        pk = random.randint(1, max_id)
        employee = Employee.objects.filter(pk=pk).first()
        if employee:
            break

    task_id = random.randint(1, 100)
    Order.objects.create(
        name="Order from celery",
        description=f"Test order#{task_id}",
        employee=employee,
        task_id=task_id,
    )

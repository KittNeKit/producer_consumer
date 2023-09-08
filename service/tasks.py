import random

from celery import shared_task

from service.models import Order, Employee


@shared_task
def create_order():
    employees = Employee.objects.all()
    random_employee = random.choice(employees)
    Order.objects.create(
        name="Order from celery",
        description="Test order",
        employee=random_employee,
        task_id=random.randint(1, 100),
    )

from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    probation = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    telegram_id = models.IntegerField()


class Order(models.Model):
    task_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

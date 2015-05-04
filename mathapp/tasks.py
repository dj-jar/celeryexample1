from __future__ import absolute_import
from celery import shared_task
from .models import AddTask, MulTask, FacTask
from django.utils import timezone


@shared_task
def add_task(a, b):
    return a + b


@shared_task
def mul_task(a, b):
    return a * b


@shared_task
def fac_task(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


@shared_task
def add_task_2(pk):
    t = AddTask.objects.get(pk=pk)
    t.result = str(add_task(t.a, t.b))
    t.end = timezone.now()
    t.save()


@shared_task
def mul_task_2(pk):
    t = MulTask.objects.get(pk=pk)
    t.result = str(mul_task(t.a, t.b))
    t.end = timezone.now()
    t.save()


@shared_task
def fac_task_2(pk):
    t = FacTask.objects.get(pk=pk)
    t.result = str(fac_task(t.n))
    t.end = timezone.now()
    t.save()

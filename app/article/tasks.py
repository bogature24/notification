from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add_task(a,b):
    print("!!!!!!!!!! 123")
    print("a", a)
    print("b", b)
    return "Hello"


@shared_task
def add_task2():
    print("!!!!!!!!!! 123 !!!!!!!!!!")
    return "Hello2"

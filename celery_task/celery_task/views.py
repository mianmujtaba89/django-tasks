from django.shortcuts import render

from .tasks import my_first_task, progress_task

def index(request):
    return render(request, 'base.html')


def task1(request):
    my_first_task.delay(10)
    return render(request, 'task1.html')


def task2(request):
    progress_task.delay(1)
    return render(request, 'task2.html')

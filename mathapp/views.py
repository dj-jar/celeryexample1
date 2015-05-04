from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from mathapp.tasks import add_task, mul_task, fac_task, add_task_2, mul_task_2, fac_task_2
from .models import AddTask, MulTask, FacTask


# ------------------------------------------------------------


# Waiting for result is OK for operarions like addition or multiplication
# since calculation is quite fast. Factorial takes a little longer.


def add_view(request, a, b):
    result = add_task(int(a), int(b))
    ctx = {
        'a': a,
        'b': b,
        'r': result
    }
    return render(request, 'mathapp/add_view.html', ctx)


def mul_view(request, a, b):
    result = mul_task(int(a), int(b))
    ctx = {
        'a': a,
        'b': b,
        'r': result
    }
    return render(request, 'mathapp/mul_view.html', ctx)


def fac_view(request, n):
    result = fac_task(int(n))
    ctx = {
        'n': n,
        'r': result
    }
    return render(request, 'mathapp/fac_view.html', ctx)


# ------------------------------------------------------------



# It does work as expected. Instead number result contains
# 'str' or '__unicode__' representation of task which is
# its UUID. But how to use it to retrieve actual result?


def add_delay_view(request, a, b):
    result = add_task.delay(int(a), int(b))
    ctx = {
        'a': a,
        'b': b,
        'r': result
    }
    return render(request, 'mathapp/add_view.html', ctx)


def mul_delay_view(request, a, b):
    result = mul_task.delay(int(a), int(b))
    ctx = {
        'a': a,
        'b': b,
        'r': result
    }
    return render(request, 'mathapp/mul_view.html', ctx)


def fac_delay_view(request, n):
    result = fac_task.delay(int(n))
    ctx = {
        'n': n,
        'r': result
    }
    return render(request, 'mathapp/fac_view.html', ctx)


# ------------------------------------------------------------


# Store data in separate model, call function which will
# run calculation function. Then redirect to task view.


def add_2_delay_view(request, a, b):
    print 'add',a,b
    t = AddTask.objects.create(
        begin=timezone.now(),
        a=a,
        b=b)
    t.save()
    x = add_task_2.delay(t.pk)
    return HttpResponseRedirect(reverse('m:task_add', args=[t.pk]))
   


def mul_2_delay_view(request, a, b):
    t = MulTask.objects.create(
        begin=timezone.now(),
        a=a,
        b=b)
    x = mul_task_2.delay(t.pk)
    return HttpResponseRedirect(reverse('m:task_mul', args=[t.pk]))


def fac_2_delay_view(request, n):
    t = FacTask.objects.create(
        begin=timezone.now(),
        n=n)
    x = fac_task_2.delay(t.pk)
    return HttpResponseRedirect(reverse('m:task_fac', args=[t.pk]))



# ------------------------------------------------------------


# View queued task.


def add_task_view(request, pk):
    t = AddTask.objects.get(pk=pk)
    ctx = {
        'a': t.a,
        'b': t.b,
        'r': t.result,
        'begin': t.begin,
        'end': t.end,
    }
    return render(request, 'mathapp/add_task_view.html', ctx)
    

def mul_task_view(request, pk):
    t = MulTask.objects.get(pk=pk)
    ctx = {
        'a': t.a,
        'b': t.b,
        'r': t.result,
        'begin': t.begin,
        'end': t.end,
    }
    return render(request, 'mathapp/mul_task_view.html', ctx)


def fac_task_view(request, pk):
    t = FacTask.objects.get(pk=pk)
    ctx = {
        'n': t.n,
        'r': t.result,
        'begin': t.begin,
        'end': t.end,
    }
    return render(request, 'mathapp/fac_task_view.html', ctx)

from django.http import HttpResponse
from django.shortcuts import render
from . models import stores
# Create your views here.


def demo(request):
    obj=stores.objects.all()
    return render(request,"index2.html",{'result':obj})


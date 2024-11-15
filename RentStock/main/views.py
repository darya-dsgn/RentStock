from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'main/catalog.html')


def profile(request):
    return render(request, 'main/profile.html')


def vxod(request):
    return render(request, 'main/vxod.html')


def catalog2(request):
    return render(request, 'main/catalog2.html')


def catalog3(request):
    return render(request, 'main/catalog3.html')
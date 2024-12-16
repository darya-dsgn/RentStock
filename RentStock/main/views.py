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


def catalogod(request):
    return render(request, 'main/catalogod.html', {})


def catalogteh(request):
    return render(request, 'main/catalogteh.html', {})
from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Home - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабинет'
    }
    return render(request, 'users/profil.html', context)


def logout(request):
    context = {
        'title': 'Home - Выход'
    }
    return render(request, '', context)
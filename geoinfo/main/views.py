from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# для заполнения navbar
menu = [
    {'title': 'О сайте', 'url_name': 'about'},
        ]


# главная страница
def main(request):

    content_mp = Continents.objects.all()           # чтение всех записей из таблицы Continents

    return render(request, 'main/main.html', {
        'menu': menu,
        'title': 'Главная страница',
        'content_mp': content_mp,
    })


# страница с информацией о сайте
def about(request):
    return render(request, 'main/about.html', {
        'menu': menu,
        'title': 'О сайте'
    })


# страница выбранного поста
@login_required                                              # допуск на страницу только авторизованных пользователей
def continent_info(request, cont):

    continent = Continents.objects.get(slug_name=cont)       # выборка необходимого континента
    cities = Cityinfo.objects.filter(cont__slug_name=cont)   # выборка городов с требуемым континентом

    return render(request, 'main/continent.html', {
        'menu': menu,
        'title': continent,
        'cont_table': cities
    })


# авторизация
def login_user(request):

    if request.method == 'POST':                                      # проверка введенных значений для авторизации
        form = LoginUserForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)                                      # авторизация пользователя
            return redirect("main")
    else:
        form = LoginUserForm()                                        # отображение пустой формы при первом посещении

    return render(request, 'main/login.html', {
        'menu': menu,
        'title': 'Авторизация',
        'form': form,
    })


# выход из профиля
def logout_user(request):
    logout(request)
    return redirect('main')


# регистрация нового пользователя
def register(request):

    if request.method == 'POST':                                      # проверка введенных значений для регистрации
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()                                        # создание учетной записи
            login(request, user)
            return redirect('main')
    else:
        form = RegisterUserForm()                                     # отображение пустой формы при первом посещении

    return render(request, 'main/register.html', {
        'menu': menu,
        'title': 'Регистрация',
        'form': form,
    })


# 404 page not found
def page_not_found(request, exception):
    return render(request, 'main/404.html', {
        'menu': menu,
        'title': '404 page not found',
    })

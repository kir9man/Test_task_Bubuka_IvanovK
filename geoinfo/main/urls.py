from django.urls import path


from . import views

urlpatterns = [
    path('', views.main, name='main'),                                              # Главная страница
    path('about/', views.about, name='about'),                                      # Раздел о сайте
    path('login/', views.login_user, name='login'),                                 # Авторизация
    path('logout/', views.logout_user, name='logout'),                              # Выход из профиля
    path('register/', views.register, name='register'),                             # Регистрация
    path('continent/<slug:cont>/', views.continent_info, name='continent_info'),    # Выбранный пост
]


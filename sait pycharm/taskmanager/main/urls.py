from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('Yan', views.Yan, name='Yan'),
    path('Danya', views.Danya, name='Danya'),
    path('Rij', views.Rij, name='Rij'),
    path('Sokrat', views.Sokrat, name='Sokrat')
]
'''
Тут мы подключаем файл views 
Из которого берём функицю index

Так же, из того же файла индекс берём функцию about
Которая отобразится на странице по адресу 
*адресс основной странички сайта*/about-us
'''
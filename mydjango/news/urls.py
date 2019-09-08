from django.contrib import admin
from django.urls import path
from . import views
from  django.conf.urls import handler400

urlpatterns = [
    path('', views.index),
    # path('login/', views.login),
    path('index/',views.login),
]

handler400=views.page_not_found
from django.urls import path
from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
    path('group_list/', views.group_list)
]
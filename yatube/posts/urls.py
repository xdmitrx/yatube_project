from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    # Главная страница
    path('posts/', views.group_list, name='group_list'),
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts),
    path('group_list/', views.group_list)
]
from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    # Главная страница
    path('posts/', views.index, name = 'posts'),
    path('posts/', views.group_posts, name ='posts')
]
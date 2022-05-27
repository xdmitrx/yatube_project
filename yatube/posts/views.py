from django.shortcuts import render, get_object_or_404
from .models import Post, Group
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)                   
                        
        
def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции'
    }
    return render(request, 'posts/group_list.html', context)


# def group_posts(request, slug):
    return HttpResponse(f'Страницы сообществ {slug}')
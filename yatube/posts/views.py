from django.shortcuts import render, get_object_or_404
from .models import Post, Group
# from django.http import HttpResponse

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'text': 'Последнее обновление на сайте.'
    }
    return render(request, 'posts/index.html', context)                   
                        
        
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Записи сообщества {slug}'
    }
    return render(request, 'posts/group_list.html', context)


# def group_posts(request, slug):
    return HttpResponse(f'Страницы сообществ {slug}')
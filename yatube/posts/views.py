from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Социальная сеть для блогеров Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)                  
                        
        
def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции'
    }
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Страницы сообществ {slug}')
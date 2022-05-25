from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)                   
                        
        
def group_posts(request, slug):
    template = 'group_posts/group_list.html'
    return render(request, template)
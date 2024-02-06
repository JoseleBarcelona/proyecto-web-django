from django.shortcuts import render
from App_blog.models import Post

# Create your views here.

def blog(request):
    
    post = Post.objects.all()
    return render(request, 'App_blog/blog.html', {'posts': post})
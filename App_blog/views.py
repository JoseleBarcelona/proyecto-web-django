from django.shortcuts import render
from App_blog.models import Post, Categoria

# Create your views here.

def blog(request):
    
    post = Post.objects.all()
    return render(request, 'App_blog/blog.html', {'posts': post})

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias=categoria)
    return render(request, 'App_blog/categorias.html', {'categoria': categoria, 'posts': post})
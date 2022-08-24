from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'blog.html', {'posts':posts,'comments':comments})


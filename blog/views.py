from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
        "title": "Post 1",
        "author": "John Doe",
        "content": "Lorem Ipsum",
        "date_posted": "01/01/2000"
    },
    {
        "title": "Post 2",
        "author": "John Smith",
        "content": "Why mr. Anderson?",
        "date_posted": "01/01/1999"
    }
]


def home(request):
    return render(request, "blog/home.html",
                  {"posts": Post.objects.all()})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

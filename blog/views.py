from django.shortcuts import render
from blog.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from auth_system.models import Author


def index(request):
    return render(
        request,
        template_name="blog/index.html"
    )

def show_posts(request):
    posts = Post.objects.all()
    context = {"post_list": posts}
    return render(
        request,
        template_name="blog/posts.html",
        context = context
    )

def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    author = Author.objects.get(id=post.author_id)
    context = {"post": post, "author":author}
    return render(
        request,
        template_name="blog/post_details.html",
        context = context
    )

def show_authors(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(
        request,
        template_name="blog/authors.html",
        context=context
    ) 

def get_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author_posts = Post.objects.filter(author_id=author_id)
    context = {"author": author, "author_posts": author_posts}
    return render(
        request,
        template_name="blog/author_posts.html",
        context=context
    )
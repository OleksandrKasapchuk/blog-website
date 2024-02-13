from django.shortcuts import render
from blog.models import Post
# Create your views here.
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
    context = {"post": post}
    return render(
        request,
        template_name="blog/post_details.html",
        context = context
    )
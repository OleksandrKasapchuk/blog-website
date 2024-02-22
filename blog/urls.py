import blog.views as blog_views
from django.urls import path

urlpatterns = [
    path("posts/", blog_views.show_posts, name="post_list"),
    path("posts/<int:post_id>/", blog_views.get_post, name="post_details"),
    path("authors/", blog_views.show_authors, name="author_list"),
    path("authors/<int:author_id>/", blog_views.get_author, name="author_posts")
]
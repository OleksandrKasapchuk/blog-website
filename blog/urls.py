import blog.views as blog_views
from django.urls import path

urlpatterns = [
    path("", blog_views.show_posts, name="post_list"),
    path("<int:post_id>/", blog_views.get_post, name="post_details")
]
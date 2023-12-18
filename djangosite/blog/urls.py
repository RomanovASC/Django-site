from django.urls import path, re_path
from . import views
from blog.views import blog_list, posts_by_blog, home_list, create_post, edit_post

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
            views.post_detail,
            name='post_detail'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:tag_name>/', posts_by_blog, name='posts_by_blog'),
    path('home/', home_list, name='home'),
    path('create-post/', create_post, name='create_post'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/edit_post/$',
            views.edit_post,
            name='edit_post'),
]


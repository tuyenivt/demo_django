from django.contrib import admin
from django.urls import path, re_path
from blog_posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('new', views.post_create, name='post_new'),
    re_path('edit/(?P<pk>\d+)', views.post_update, name='post_edit'),
    re_path('delete/(?P<pk>\d+)', views.post_delete, name='post_delete'),
]

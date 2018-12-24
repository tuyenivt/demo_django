from django.contrib import admin
from django.urls import path, re_path, include
import blog.views
import blog.urls

urlpatterns = [
    re_path('^$', blog.views.HomeView.as_view(), name='home'),
    re_path('^', include(blog.urls)),
    path('admin/', admin.site.urls),
]

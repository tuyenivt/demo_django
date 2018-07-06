from django.shortcuts import render
from django.forms import ModelForm

from blog_posts.models import blog_posts
# Create your views here.


class PostsForm(ModelForm):
    class Meta:
        model = blog_posts
        friends = ['id', 'title', 'author']


def post_list(request, template_name='blog_posts/post_list.html'):
    posts = blog_posts.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

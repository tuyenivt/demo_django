# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class blog_posts(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})

from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^(?P<pk>\d+)$', views.EntryDetail.as_view(), name="entry_detail"),
]

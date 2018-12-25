from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import Entry

class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

class EntryDetail(DetailView):
    model = Entry
    template_name = 'blog/entry_detail.html'
    form_class = CommentForm

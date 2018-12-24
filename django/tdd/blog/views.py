from django.views.generic import ListView
from .models import Entry

class HomeView(ListView):
    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.


def login(request):
    if False:
        return HttpResponseRedirect('audit:defect')
    else:
        return render(request, 'audit/login.html', {
            'error_message': "Your username or password is wrong."
        })


class DefectIndexView(generic.ListView):
    template_name = 'audit/defect/index.html'


class DefectAddView(generic.DetailView):
    template_name = 'audit/defect/add.html'


class DefectUpdateView(generic.DetailView):
    template_name = 'audit/defect/update.html'


def remove(request, defect_id):
    return HttpResponseRedirect('audit:defect')

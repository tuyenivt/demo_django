from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic

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

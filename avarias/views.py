from django.shortcuts import render, redirect
from avarias.models import Avaria
from avarias.forms import  AvariasModelForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.'''


class AvariasView(View):
    
    def get(self, request):
        avarias = Avaria.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            avarias = avarias.filter(model__icontains = search)

        return render(request,'avarias.html',{'avarias': avarias})


class AvariasListView(ListView):
    model = Avaria 
    template_name = 'avarias.html' 
    context_object_name = 'avarias'

    def get_queryset(self):
        avarias = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            avarias = avarias.filter(model__icontains = search)
        return avarias

@method_decorator(login_required(login_url='login_view'), name='dispatch')
class NewAvariasView(CreateView):
    model = Avaria
    template_name = "new_avarias.html"
    form_class = AvariasModelForm
    success_url = "/avarias/"



class AvariaDetailView(DetailView):
    model = (Avaria)
    template_name = "avarias_detail.html"


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaUpdateView(UpdateView):
    model = Avaria
    form_class = AvariasModelForm
    template_name = 'avaria_update.html'
    success_url = "/avarias/"


    def get_success_url(self):
        return reverse_lazy('avarias_detail', kwargs = {'pk': self.object.pk})


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaDeleteView(DeleteView):
    model = Avaria
    template_name = 'avaria_delete.html'
    

    def get_success_url(self):
        return '/avarias/'



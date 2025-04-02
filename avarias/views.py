from django.shortcuts import render, redirect, get_object_or_404
from avarias.models import Avaria, ImagemReferencia
from avarias.forms import  AvariasModelForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import ImagemModelForm
from django.urls import reverse
from django.contrib import messages

from django.forms import modelformset_factory
# Create your views here.'''


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaImagemCreateView(CreateView):
    model = Avaria
    form_class = AvariasModelForm
    template_name = 'new_avarias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        ImagemFormSet = modelformset_factory(ImagemReferencia, form=ImagemModelForm, extra=3)  
        context['imagem_formset'] = ImagemFormSet(queryset=ImagemReferencia.objects.none())
        return context

    def form_valid(self, form):
       
        avaria = form.save()
       
        imagem_formset = modelformset_factory(ImagemReferencia, form=ImagemModelForm)( self.request.POST, self.request.FILES)
        if imagem_formset.is_valid():
            if len(imagem_formset) != 3:
                form.add_error(None, "Você deve preencher todos os campos IMAGENS.")
                return self.form_invalid(form)
            for imagem_form in imagem_formset:
                if imagem_form.is_valid():
                    imagem = imagem_form.save(commit=False)
                    imagem.avaria = avaria  
                    imagem.save()     
        self.object = avaria
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        
        return reverse('avarias_detail', kwargs={'pk': self.object.id})
    
  
class AvariasView(View):
    
    def get(self, request):
        avarias = Avaria.objects.all().order_by('modelo')
        search = request.GET.get('search')
        if search:
            avarias = avarias.filter(model__icontains = search)

        return render(request,'avarias.html',{'avarias': avarias})


class AvariasListView(ListView):
    model = Avaria 
    template_name = 'avarias.html' 
    context_object_name = 'avarias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        for avaria in context['avarias']:
            avaria.primeira_imagem = avaria.imagens.first() 

        return context
    def get_queryset(self):
        avarias = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')
        if search:
            avarias = avarias.filter(model__icontains = search)
        return avarias




class AvariaDetailView(DetailView):
    model = Avaria
    template_name = 'avarias_detail.html'
    context_object_name = 'avaria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avaria = self.get_object()
        
        
        primeira_imagem = avaria.imagens.first()  
        
        context['primeira_imagem'] = primeira_imagem
        return context


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaUpdateView(UpdateView):
    model = Avaria
    form_class = AvariasModelForm
    template_name = 'avaria_update.html'
    success_url = "/avarias/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        avaria = self.get_object()
        imagens = avaria.imagens.all()
        
        
        ImagemReferenciaFormSet = modelformset_factory(ImagemReferencia, form=ImagemModelForm, extra=0)
        formset = ImagemReferenciaFormSet(queryset=imagens)
        
        context['formset'] = formset
        return context

    def form_valid(self, form):
        
        avaria = form.save(commit=False)
        avaria.save()
        
        
        formset = modelformset_factory(ImagemReferencia, form=ImagemModelForm,)
        imagens_formset = formset(self.request.POST, self.request.FILES, queryset=avaria.imagens.all())
        
        if imagens_formset.is_valid():
            for imagem_form in imagens_formset:
                imagem_form.save()

            messages.success(self.request, "Avaria e imagens atualizadas com sucesso!")
            return redirect('avarias_detail', pk=avaria.pk)
        else:
            messages.error(self.request, "Erro ao atualizar as imagens.")
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    


@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaDeleteView(DeleteView):
    model = Avaria
    template_name = 'avaria_delete.html'
    

    def get_success_url(self):
        return '/avarias/'


def detalhes_avaria(request, avaria_id):
    avaria = get_object_or_404(Avaria, id=avaria_id)
    return render(request, 'detalhes_imagens.html', {'avaria': avaria})
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

from django.forms import modelformset_factory
# Create your views here.'''


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

        # Para cada avaria, buscamos a primeira imagem
        for avaria in context['avarias']:
            avaria.primeira_imagem = avaria.imagens.first()  # Atribui a primeira imagem à avaria

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
        
        # Pegar a primeira imagem relacionada à avaria (se houver)
        primeira_imagem = avaria.imagens.first()  # 'imagens' é o campo relacionado no modelo Avaria
        
        context['primeira_imagem'] = primeira_imagem
        return context


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



@method_decorator(login_required(login_url='login_view'), name='dispatch')
class AvariaImagemCreateView(CreateView):
    model = Avaria
    form_class = AvariasModelForm
    template_name = 'new_avarias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Criar um formset para múltiplas imagens
        ImagemFormSet = modelformset_factory(ImagemReferencia, form=ImagemModelForm, extra=3)  # extra=3 cria 3 formulários em branco
        context['imagem_formset'] = ImagemFormSet(queryset=ImagemReferencia.objects.none())
        return context

    def form_valid(self, form):
        # Salva a avaria
        avaria = form.save()
        print('avaria foi salva!')
        # Processa o formset de imagens
        imagem_formset = modelformset_factory(ImagemReferencia, form=ImagemModelForm)(self.request.POST, self.request.FILES)

        if imagem_formset.is_valid():
            print(f"Formulários válidos: {len(imagem_formset.cleaned_data)}")
            for imagem_form in imagem_formset:
                if imagem_form.is_valid():
                    print(f"Formulário válido: {imagem_form.cleaned_data}")
                    imagem = imagem_form.save(commit=False)
                    imagem.avaria = avaria  # Associa a imagem à avaria
                    imagem.save()
                    print(f"Imagem {imagem.imagem.name} salva com sucesso!")  # Mensagem de depuração
                else:
                    print(f"Erros no formulário: {imagem_form.errors}")

            

        # Atribui a avaria salva a self.object
        
        else:
            print("Formset de imagens não é válido!")
            print(imagem_formset.errors)  # Exibe os erros de validação
            
        self.object = avaria
        # Redireciona para a URL de sucesso usando o ID da avaria
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # Usa o reverse para gerar a URL correta com o ID da avaria
        return reverse('avarias_detail', kwargs={'pk': self.object.id})


def detalhes_avaria(request, avaria_id):
    avaria = get_object_or_404(Avaria, id=avaria_id)
    return render(request, 'detalhes_imagens.html', {'avaria': avaria})
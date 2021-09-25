from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo


from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'cpf', 'etapa']
    template_name = 'form.html'
    success_url = reverse_lazy('lista-campo')

############################ UPDATE

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'cpf', 'etapa']
    template_name = 'form.html'
    success_url = reverse_lazy('lista-campo')

############################# DELETE

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('index')


############################# LISTA

class CampoList(ListView):
    model = Campo
    template_name = 'lista-campo.html'
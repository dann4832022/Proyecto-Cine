from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView

from .forms import OpinionForm
from .models import Opinion

# Create your views here.


def AgregarOpinion(request):
    form = OpinionForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    contexto = {
        
        'form': form,
    }
    template_name = 'opiniones/agregar_opinion.html'
    return render(request, template_name, contexto)


class Modificar_opinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['texto']
    template_name = 'opiniones/agregar_opinion.html'
    success_url = reverse_lazy('apps.cine:listar_cine')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)


class EliminarOpinion(LoginRequiredMixin, DeleteView):
    model = Opinion
    template_name = 'cine/confirma_eliminar.html'
    success_url = reverse_lazy("apps.cine:listar_cine")
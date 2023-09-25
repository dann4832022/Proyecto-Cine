from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models.query import QuerySet
from typing import Any

# Create your views here.
from .models import Categorias, Cine
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

class AgregarCategoria(CreateView, LoginRequiredMixin):
    model = Categorias
    fields = ['nombre']
    template_name = 'cine/agregar_categoria.html'
    success_url = reverse_lazy('inicio')

class ModificarCine(LoginRequiredMixin, UpdateView):
    model = Cine
    fields = ['titulo', 'autor', 'descripcion', 'imagen', 'categoria']
    template_name = 'cine/agregar_cine.html'
    success_url = reverse_lazy('apps.cine:listar_cine')


class AgregarCine(CreateView, LoginRequiredMixin):
    model = Cine
    fields = ['titulo', 'autor', 'descripcion', 'imagen', 'categoria']
    template_name = 'cine/agregar_cine.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)

class EliminarCine(LoginRequiredMixin, DeleteView):
    model = Cine
    template_name = 'cine/confirma_eliminar.html'
    success_url = reverse_lazy('apps.cine:listar_cine')

class ListarCine(ListView):
    model = Cine
    template_name = 'cine/listar_cine.html'
    context_object_name = "cine"
    # -----Paginación------
    # paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['categorias'] = categorias
        return context


    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')
    


def ListarCinePorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre=categoria)
    libros = Cine.objects.filter(
        categoria=categorias2[0].id).order_by('fecha_agregado')
    categorias = Categorias.objects.all()
    template_name = 'cine/listar_cine.html'
    contexto = {
        'cine': libros,
        'categorias': categorias
    }
    return render(request, template_name, contexto)

def cine_detalle(request, id):
    cine = Cine.objects.get(id=id)
    opiniones = Opinion.objects.filter(libro=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.libro = cine
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'cine': cine,
        'form': form,
        'opiniones': opiniones,
    }
    template_name = 'cine/cine.html'
    return render(request, template_name, contexto)




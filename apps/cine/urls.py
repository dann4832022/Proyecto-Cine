from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from .views import AgregarCategoria, AgregarCine, ModificarCine, EliminarCine, ListarCine, ListarCinePorCategoria, cine_detalle
app_name = 'apps.cine'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(),name='agregar_categoria'),
    path("agregar_cine/", AgregarCine.as_view(), name='agregar_cine'),
    path("modificar_cine/<int:pk>", ModificarCine.as_view(), name='modificar_cine'),
    path("eliminar_cine/<int:pk>", EliminarCine.as_view(), name='eliminar_cine'),
    path("listar_cine/", ListarCine.as_view(), name='listar_cine'),
    path("listar_por_categoria/<str:categoria>", ListarCinePorCategoria, name='listar_por_categoria'),
    path("cine_detalle/<int:id>", cine_detalle, name='cine_detalle'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
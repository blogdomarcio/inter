
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^estilo^$', views.estilo, name='estilo'),
    url(r'^comodos/estilo/(?P<estilo_id>\d+)', views.comodos, name='lista_comodos'),
    url(r'^quarto/estilo/(?P<estilo_id>\d+)', views.quarto, name='lista_quarto'),
    url(r'^cozinha/estilo/(?P<estilo_id>\d+)', views.cozinha, name='lista_cozinha'),
    url(r'^sala/estilo/(?P<estilo_id>\d+)', views.sala, name='lista_sala'),
    url(r'^lavabo/estilo/(?P<estilo_id>\d+)', views.lavabo, name='lista_lavabo'),
    url(r'^externa/estilo/(?P<estilo_id>\d+)', views.externa, name='lista_externa'),
    url(r'^lavanderia/estilo/(?P<estilo_id>\d+)', views.lavanderia, name='lista_lavanderia'),
    url(r'^varanda/estilo/(?P<estilo_id>\d+)', views.varanda, name='lista_varanda'),
    url(r'^outros/estilo/(?P<estilo_id>\d+)', views.outros, name='lista_outros'),



]

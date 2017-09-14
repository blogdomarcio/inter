
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^estilo^$', views.estilo, name='estilo'),
    url(r'^comodos/estilo/(?P<estilo_id>\d+)', views.comodos, name='lista_comodos'),


]

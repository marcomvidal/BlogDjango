from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postagens_listar, name='postagens_listar'),
    url(r'^postagens/(?P<pk>[0-9]+)/$', views.postagens_detalhes, name='postagens_detalhes'),
    url(r'^postagens/criar/$', views.postagens_criar, name='postagens_criar'),
    url(r'^postagens/(?P<pk>[0-9]+)/editar/$', views.postagens_editar, name='postagens_editar'),
    url(r'^postagens/(?P<pk>[0-9]+)/excluir/$', views.postagens_excluir, name='postagens_excluir'),
]



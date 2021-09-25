from django.urls import path

#importa as views criadas
from .views import CampoCreate
from .views import CampoUpdate
from .views import CampoDelete
from .views import CampoList

urlpatterns = [
   #campo para a criacao
   path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),

   #campo para os updates
   path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),

   #campo para o delete
   path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),

   #campo de lista
   path('lista/campo', CampoList.as_view(), name='lista-campo')

]

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.appHome, name='appHome' ),

    #adicionar lemmings:
    path('adicionar', views.add_usuario, name="add_usuario"),

    #editar lemmings:
    path('editar/<int:id_usuario>', views.editar_usuario, name="editar_usuario"),

    #excluir lemmings:
    path('excluir/<int:id_usuario>', views.excluir_usuario, name="excluir_usuario"),
]
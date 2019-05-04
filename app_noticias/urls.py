from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePageView.as_view(), name='home'),
    path('noticia/contato/', ContatoView.as_view(), name='contato')
    path('noticia/contato/sucesso', ContatoSucessoView.as_view(), name='sucesso')
    
]
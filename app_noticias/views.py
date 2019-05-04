from django.shortcuts import render
from django.views.generic import ListView

from .models import Noticia
# Create your views here.
class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem.dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_sucess_url(self):
        return reverse('contato_sucesso')

class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/contato_sucesso.html'
from django.db import models
class Noticia(models.Model):
    conteudo = models.TextField()
    titulo = models.CharField('título', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField('Data da Criação')
    data_publicacao = models.DateTimeField('Data da publicação')
    publicado = models.BooleanField('Publicado')
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    def __str__(self):
        return self.titulo
# Create your models here.

class MensagemDeContato(models.Model)
    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de contato'

    name = models.CharField(max_length=128)
    email = models.EmailField('E-mail', null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(MensagemDeContato)
calss MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)
from django.contrib import admin
from .models import Contacto
# Register your models here.

@admin.register(Contacto)
class ContactoAdin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'assunto']
    search_fields = ['mensagem', 'email', 'nome']

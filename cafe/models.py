from django.db import models

# Create your models here.
class Contacto(models.Model):

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()


    def __str__(self):
        return self.nome
    


class Reserva(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateField()
    tempo = models.TimeField()
    pessoas = models.PositiveIntegerField()
    mensagem = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.nome} para {self.pessoas} pessoa(s) em {self.data} às {self.tempo}"
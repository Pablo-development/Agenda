from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)#parametros para nao ser obrigatorio adicionar desc
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)#parametro para que toda vez que for adicionado um evendo, seja utilizado a data e hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #caso usuario seja excluido, CASCADE exclui o usuario
    local = models.TextField(blank=True, null=True)
    class Meta: #forma de forçar com que o nome da tabela no db seja a escolhida abaixo
        db_table = 'evento'

    def __str__(self):  #Serve para que o banco de dados saiba como tratar os objetos, retornando eles com os nomes inseridos no db
        return self.titulo
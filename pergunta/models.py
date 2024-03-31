from django.db import models

# Create your models here.
class Area(models.Model):

    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Materia(models.Model):
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Pergunta(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    enuciado = models.CharField(max_length=505)
    resposta = models.CharField(max_length=200)
    assunto  = models.CharField(max_length=200)
    resolucao  = models.CharField(max_length=500)
    foto = models.ImageField()

    def __str__(self):
        return self.assunto


class Pergunta_simulado(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.DO_NOTHING)
    respondido = models.BooleanField(default=False)
    acertou = models.BooleanField(default=False)
    

class Simulado(models.Model):
    nome = models.CharField(max_length=50)
    area_pertence = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING, default='todas')
    quantidade = models.IntegerField()
    feito = models.IntegerField(default=0) 

    def __str__(self):
        return self.nome
    
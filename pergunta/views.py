from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Area, Materia, Pergunta, Pergunta_simulado, Simulado


def criar(request):
   if request.method == 'GET':
        materia = Materia.objects.all()
        return render(request, 'criar_pergunta.html', {'materia': materia})
      
   elif request.method =='POST':
      pergunta= request.POST.get('question')
      res = request.POST.get('res')
      materia = request.POST.get('materia')
      assunto = request.POST.get('assunto')
      resolucao = request.POST.get('resolucao')

      criar =  Pergunta(
         
         materia_id = materia,
         enuciado=pergunta,
         resposta=res,
         assunto = assunto,
         resolucao = resolucao

      )

      criar.save()

      return HttpResponse('Deu certo')


def criar_simulado(request):
   if request.method == 'GET':
      area = Area.objects.all()
      materia = Materia.objects.all()
      return render(request, 'criar_simulado.html', {'area': area, 'materia': materia})

      
   elif request.method == 'POST':
      nomesimulado = request.POST.get('nomesimulado')
      categoriasimulado = request.POST.get('categoriasimulado')
      materiasimulado = request.POST.get('materiasimulado')
      qtd = request.POST.get('qtd')

      criar_simulado = Simulado(

         nome=nomesimulado,
         area_pertence_id=categoriasimulado,
         materia_id=materiasimulado,
         quantidade=qtd,

      )      
      criar_simulado.save()

      return redirect('/pergunta/criar_pergunta/')

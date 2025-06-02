from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages
from .models import Contacto, Reserva
from django.urls import reverse
# Create your views here.

#PAGINA PRINCIPAL DO SITE
def home(request):
    return render(request, 'index.html')


def contacto(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    elif request.method == 'POST':

        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        assunto = request.POST.get('assunto', '').strip()
        mensagem = request.POST.get('mensagem', '').strip()

       
        if not nome or not email or not assunto or not mensagem:
            messages.add_message(request, constants.WARNING, 'Todos os campos são obrigatórios.')
            return redirect('contacto')
        
        try:
            contacto = Contacto.objects.create(
                nome=nome,
                email=email,
                assunto=assunto,
                mensagem=mensagem
            )
            contacto.save()
            messages.add_message(request, constants.SUCCESS, 'Mensagem enviada com sucesso!')
            return redirect('contacto')

        except Exception as e:   
            messages.add_message(request, constants.DEBUG, 'Mensagem não enviada. Tente novamente mais tarde.')
            return redirect('contacto')



    return render(request, 'index.html')



def reservas(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    

    elif request.method == 'POST':
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        telefone = request.POST.get('telefone', '')
        data = request.POST.get('data', '')
        tempo = request.POST.get('tempo', '')
        pessoas = request.POST.get('pessoas', '')
        mensagem = request.POST.get('mensagem', '')

    # Validação simples (podes personalizar ou reforçar)
    if not nome or not email or not data or not tempo or not pessoas:
        messages.add_message(request, constants.ERROR, 'Todos os campos obrigatórios devem ser preenchidos.')
        return redirect('/#reservas')

    try:
        # Aqui assumes que tens um modelo chamado Reserva
        Reserva.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            data=data,
            tempo=tempo,
            pessoas=pessoas,
            mensagem=mensagem
        )
        messages.add_message(request, constants.SUCCESS, 'Reserva enviada com sucesso!')
    except Exception as e:
        messages.add_message(request, constants.ERROR, 'Informamos que, neste momento, não estamos a aceitar reservas de mesa.')

    return redirect('/#reserva')



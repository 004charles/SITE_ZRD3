from django.shortcuts import render, HttpResponse
from .models import Testemunho, Equipe, Contactar, Cliente

def index (request):
    testemunho = Testemunho.objects.all()
    equipe = Equipe.objects.all()
    cliente = Cliente.objects.all()
    return render( request, 'index.html', {'testemunho': testemunho, 'equipe': equipe, 'cliente':cliente  })

def contactar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        descricao = request.POST.get('menssagem')
        
        contactar = Contactar(nome=nome, email=email, assunto=assunto, descricao=descricao)
        contactar.save()

        return HttpResponse("Mensagem enviada com sucesso, Obrigado!")
    return render(request, 'index.html')

def perfil(request, id):
    equipe = Equipe.objects.filter(id=id)
    return render(request, 'perfil.html',{'equipe': equipe})
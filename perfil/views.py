from django.shortcuts import render

# Create your views here.
from perfil.models import Banheiro, Estilo, Quarto, Sala


def home(request):
    estilos = Estilo.objects.all()

    context = {
        'estilos': estilos,

    }

    return render(request, 'perfil/home.html', context)


def estilo(request):
    banheiros = Banheiro.objects.all()

    context = {
        'banheiros': banheiros,

    }

    return render(request, 'perfil/estilo.html', context)


def comodos(request, estilo_id):
    quarto = Quarto.objects.filter(estilo__quarto=estilo_id).first()
    sala = Sala.objects.filter(estilo__sala=estilo_id).first()

    context = {

        'quarto': quarto,
        'sala':sala,

    }

    return render(request, 'perfil/comodos.html', context)


def banheiro(request):
    banheiros = Banheiro.objects.all()

    context = {
        'banheiros': banheiros,

    }

    return render(request, 'perfil/banheiro.html', context)

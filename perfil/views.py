from django.shortcuts import render

# Create your views here.
from perfil.models import Estilo, Quarto, Sala, Cozinha, Lavabo, Externa, Lavanderia, Outros, Varanda


def home(request):
    estilos = Estilo.objects.all()

    context = {
        'estilos': estilos,

    }

    return render(request, 'perfil/home.html', context)


def estilo(request):
    lavabo = Lavabo.objects.all()

    context = {
        'lavabo': lavabo,

    }

    return render(request, 'perfil/estilo.html', context)


def comodos(request, estilo_id):

    estilos = Estilo.objects.all()
    quarto = Quarto.objects.filter(estilo__exact=estilo_id).first()
    sala = Sala.objects.filter(estilo__exact=estilo_id).first()
    cozinha = Cozinha.objects.filter(estilo__exact=estilo_id).first()
    lavabo = Lavabo.objects.filter(estilo__exact=estilo_id).first()
    externa = Externa.objects.filter(estilo__exact=estilo_id).first()
    lavanderia = Lavanderia.objects.filter(estilo__exact=estilo_id).first()
    outros = Outros.objects.filter(estilo__exact=estilo_id).first()
    varanda = Varanda.objects.filter(estilo__exact=estilo_id).first()

    context = {
        'estilos':estilos,
        'lavabo':lavabo,
        'quarto': quarto,
        'sala':sala,
        'cozinha':cozinha,
        'externa':externa,
        'lavanderia':lavanderia,
        'outros':outros,
        'varanda':varanda,

    }

    return render(request, 'perfil/comodos.html', context)


def quarto(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Quarto.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/quarto.html', context)


def sala(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Sala.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/sala.html', context)


def cozinha(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Cozinha.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/cozinha.html', context)


def lavabo(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Lavabo.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/lavabo.html', context)


def externa(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Externa.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/externa.html', context)


def lavanderia(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Lavanderia.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/lavanderia.html', context)



def varanda(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Varanda.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/varanda.html', context)


def outros(request, estilo_id):

    est = Estilo.objects.all()

    quartos = Outros.objects.filter(estilo__exact=estilo_id)

    context = {
        'quartos': quartos,
        'est': est,

    }

    return render(request, 'perfil/outros.html', context)


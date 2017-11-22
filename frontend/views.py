from django.shortcuts import render,redirect
from game.models import Juego
from game.forms import FormJuego


# Create your views here.
def home_juegos(request):
    return render(request, 'index.html',{})


def v_juegos(request):
    return render(request, 'juegos.html',{})

def v_juego(request,id):
    juego= Juego.objects.get(id=id)

    return render(request,'juego.html',{'juego':juego})

def v_update(request,id):
    juego= Juego.objects.get(id=id)
    print(juego.nombre)
    if request.method=="POST":

        form = FormJuego(request.POST,instance=Juego)
        if form.is_valid():
            form.save()
            return redirect ('/juegos/')
    else:
        form=FormJuego(instance=juego)
        print(form)

    return render(request, 'nuevo.html', {'form': form, 'funcion': 'Actualizar'})






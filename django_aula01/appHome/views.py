from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from appHome.models import Usuario
from appHome.forms import FormUsuario


#Adicionar
def add_usuario(request):
    formUsuario = FormUsuario(request.POST or None)

    if request.POST:
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('appHome')

    context = { 
        'form' : formUsuario
    }
    return render (request, 'add_usuario.html', context)


#Editar
def editar_usuario(request, id_usuario):

    #Verifica se o id passado como parâmetro da função existe no bd:
    usuario = Usuario.objects.get(id=id_usuario)

    formUsuario = FormUsuario(request.POST or None, instance=usuario)

    if request.POST:
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('appHome')

    context = { 
        'form' : formUsuario
    }
    return render (request, 'editar_usuario.html', context)



#Excluir
def excluir_usuario(request, id_usuario):

    #Verifica se o id passado como parâmetro da função existe no bd:
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect('appHome')




def appHome(request):

    usuario = Usuario.objects.all()

    dados = {
        'usuarios' : usuario
    }

    pagina = loader.get_template('home.html')
    return HttpResponse(pagina.render(dados))

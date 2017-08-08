from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Postagem
from .forms import PostagemForm


def postagens_listar(request):
    '''Listagem de todas as postagens'''
    postagens = Postagem.objects.filter(publicado=True)\
                                .order_by('-data_publicacao')

    contexto = {
        'postagens': postagens
    }

    return render(request, 'postagens/postagens_listar.html', contexto)


@login_required
def postagens_rascunhos(request):
    '''Listagem de todas as postagens que ainda não foram publicadas'''
    postagens = Postagem.objects.filter(publicado=False) \
                                .order_by('-data_criacao')

    contexto = {
        'postagens': postagens
    }

    return render(request, 'postagens/postagens_rascunhos.html', contexto)


@login_required
def postagens_publicar(request, pk):
    '''Publicação de postagens rascunho'''
    postagem = get_object_or_404(Postagem, pk=pk)
    postagem.publicar()

    return redirect('postagens_detalhes', pk=pk)


def postagens_detalhes(request, pk):
    '''Listagem de uma postagem específica'''
    postagem = get_object_or_404(Postagem, pk=pk)

    contexto = {
        'postagem': postagem
    }

    if request.POST:
        if request.POST.get('email', None):

            if postagem.enviar(request.POST['email']):
                contexto['mail_result'] = 'Enviado'
            else:
                contexto['mail_result'] = 'E-mail inválido'
        else:
            contexto['mail_result'] = 'Preencha o email'

    return render(request, 'postagens/postagens_detalhes.html', contexto)


@login_required
def postagens_criar(request):
    '''Criação de uma nova postagem'''
    formulario = PostagemForm(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            postagem = formulario.save(commit=False)
            postagem.autor = request.user
            postagem.save()

            if postagem.publicado:
                postagem.publicar()

            return redirect('postagens_detalhes', pk=postagem.pk)

    contexto = {
        'formulario': formulario
    }

    return render(request, 'postagens/postagens_editar.html', contexto)


@login_required
def postagens_editar(request, pk):
    '''Edição de uma postagem existente'''
    postagem = get_object_or_404(Postagem, pk=pk)

    if request.method == "POST":
        formulario = PostagemForm(request.POST, instance=postagem)
        if formulario.is_valid():
            postagem = formulario.save(commit=False)
            postagem.autor = request.user
            postagem.save()

            if postagem.publicado:
                postagem.publicar()
            else:
                postagem.data_publicacao = ""
                postagem.publicado = False

            return redirect('postagens_detalhes', pk=postagem.pk)
    else:
        formulario = PostagemForm(instance=postagem)

    contexto = {
        'formulario': formulario
    }

    return render(request, 'postagens/postagens_editar.html', contexto)


@login_required
def postagens_excluir(request, pk):
    '''Exclusão de uma postagem existente'''
    postagem = Postagem.objects.filter(pk=pk)
    postagem.delete()

    return redirect('postagens_listar')
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postagem
from .forms import PostagemForm


def postagens_listar(request):
    '''Listagem de todas as postagens'''
    postagens = Postagem.objects.filter(data_publicacao__lte=timezone.now())\
                                .order_by('-data_publicacao')
    contexto = {
        'postagens': postagens
    }

    return render(request, 'postagens/postagens_listar.html', contexto)


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


def postagens_criar(request):
    '''Criação de uma nova postagem'''

    formulario = PostagemForm(request.POST or None)

    if request.POST:
        if formulario.is_valid():
            postagem = formulario.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('postagens_detalhes', pk=postagem.pk)

    contexto = {
        'formulario': formulario
    }

    return render(request, 'postagens/postagens_editar.html', contexto)


def postagens_editar(request, pk):
    '''Edição de uma postagem existente'''
    postagem = get_object_or_404(Postagem, pk=pk)

    formulario = PostagemForm(request.POST or None, instance=postagem)

    #if request.method == "POST":
    if request.POST:
        #formulario = PostagemForm(request.POST)
        if formulario.is_valid():
            postagem = formulario.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('postagens_detalhes', pk=postagem.pk)
    #else:
    #    formulario = PostagemForm(instance=postagem)

    contexto = {
        'formulario': formulario
    }

    return render(request, 'postagens/postagens_editar.html', contexto)


def postagens_excluir(request, pk):
    '''Exclusão de uma postagem existente'''
    postagem = Postagem.objects.filter(pk=pk)
    postagem.delete()

    return redirect('postagens_listar')
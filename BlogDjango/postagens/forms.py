from django import forms
from .models import Postagem


class PostagemForm(forms.ModelForm):
    #titulo = forms.CharField(widget=forms.TextInput(attrs={
    #    'class' : 'form-control',
    #    'placeholder': 'Assunto da postagem'
    #}))
    #descricao = forms.CharField(widget=forms.Textarea(attrs={
    #    'class' : 'form-control',
    #    'rows' : 3,
    #    'placeholder': 'Texto exibido na página inicial e no cabeçalho da postagem'
    #}))
    #conteudo = forms.CharField(widget=forms.Textarea(attrs={
    #    'class' : 'form-control',
    #    'rows': 15,
    #    'placeholder': 'Texto principal da postagem'
    #}))

    class Meta:
        model = Postagem
        fields = ('titulo', 'descricao', 'conteudo')
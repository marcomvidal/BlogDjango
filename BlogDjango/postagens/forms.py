from django import forms
from .models import Postagem


class PostagemForm(forms.ModelForm):
    publicado = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = Postagem
        fields = ('titulo', 'descricao', 'conteudo', 'publicado')
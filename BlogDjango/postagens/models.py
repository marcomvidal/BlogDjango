from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone

from BlogDjango.settings import EMAIL_HOST_USER


class Postagem(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conteudo = models.TextField()
    publicado = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.publicado = True
        self.data_publicacao = timezone.now()
        self.save()

    def enviar(self, destinatario):
        try:
            mail = destinatario
            validate_email(mail)
        except ValidationError:
            mail = None

        if mail:
            send_mail(
                self.titulo,
                self.conteudo,
                EMAIL_HOST_USER,
                [mail],
                fail_silently=False,
            )
            return True

        return False

    def __str__(self):
        return self.titulo
from django.contrib import admin
from .models import Postagem

# Register your models here.


class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo',)
    actions = ['enviar']

    def enviar(modeladmin, request, queryset):
        for postagem in queryset:
            postagem.enviar('marcomvidal@gmail.com')
    enviar.short_description = "Enviar para Marco"

admin.site.register(Postagem, PostagemAdmin)
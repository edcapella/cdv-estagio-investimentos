from django.contrib import admin
from .models import Campo

# Register your models here.

@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'etapa')
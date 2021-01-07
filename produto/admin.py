from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'ativo', 'price')


admin.site.register(Produto, ProdutoAdmin)
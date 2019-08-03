from django.contrib import admin
from .models import Entrada, Aspirantes, Archivos
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(MarkdownxModelAdmin):
    pass

admin.site.register(Aspirantes)
admin.site.register(Archivos)






#admin.site.register(MyModel, MarkdownxModelAdmin)
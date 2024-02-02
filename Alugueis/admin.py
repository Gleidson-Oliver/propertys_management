from django.contrib import admin

from Pagamentos.models import PagamentosJaneiro

from .models import Casa, Inquilino

# Register your models here.
admin.site.register(Casa)
admin.site.register(Inquilino)
admin.site.register(PagamentosJaneiro)

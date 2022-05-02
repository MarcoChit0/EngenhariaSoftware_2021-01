from django.contrib import admin
from usuario.models import Cliente, Medico, Professor

admin.site.register(Professor)
admin.site.register(Medico)
admin.site.register(Cliente)



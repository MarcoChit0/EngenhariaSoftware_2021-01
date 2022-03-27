from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Professor)
admin.site.register(Medico)
admin.site.register(Cliente)
admin.site.register(Especialidade)
admin.site.register(Aula)
admin.site.register(Consulta)
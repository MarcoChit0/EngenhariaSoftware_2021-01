from django.contrib import admin
from .models import User, Professional, Client, Professor, Doctor

# Register your models here.
admin.site.register(User)
admin.site.register(Professor)
admin.site.register(Doctor)
admin.site.register(Client)
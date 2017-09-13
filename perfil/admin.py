from django.contrib import admin

# Register your models here.
from .models import Banheiro, Cozinha, Quarto, Sala

admin.site.register(Banheiro)
admin.site.register(Cozinha)
admin.site.register(Quarto)
admin.site.register(Sala)
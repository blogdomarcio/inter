from django.contrib import admin

# Register your models here.
from .models import Cozinha, Quarto, Sala, Estilo, Lavabo, Outros, Varanda, Lavanderia, Externa

admin.site.register(Lavabo)
admin.site.register(Cozinha)
admin.site.register(Quarto)
admin.site.register(Sala)
admin.site.register(Estilo)
admin.site.register(Outros)
admin.site.register(Varanda)
admin.site.register(Lavanderia)
admin.site.register(Externa)

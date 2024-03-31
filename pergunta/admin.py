from django.contrib import admin
from .models import Area, Materia, Pergunta, Pergunta_simulado, Simulado
# Register your models here.
admin.site.register(Area)
admin.site.register(Materia)
admin.site.register(Pergunta)
admin.site.register(Pergunta_simulado)
admin.site.register(Simulado)
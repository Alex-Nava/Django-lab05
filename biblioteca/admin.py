from django.contrib import admin

from .models import Libro, Usuario, Review

admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Review)

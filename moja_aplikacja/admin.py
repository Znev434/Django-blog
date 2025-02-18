from django.contrib import admin
from .models import Post  # Importujemy nasz model Post

admin.site.register(Post)  # Rejestrujemy model Post w panelu administracyjnym

from django.contrib import admin
from django.urls import path, include
from moja_aplikacja import views  # ✅ Importuj z aplikacji, NIE z projektu

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel administracyjny
    path('', include('moja_aplikacja.urls')),  # Ładuje ścieżki z aplikacji
    path('test-message/', views.test_message, name='test_message'),  # Test komunikatów
]

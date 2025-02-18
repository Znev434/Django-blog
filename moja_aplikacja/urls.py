from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Strona główna
    path('add/', views.add_post, name='add_post'),  # Dodawanie posta
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),  # Edytowanie posta
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),  # Usuwanie posta
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Wyświetlanie posta
]

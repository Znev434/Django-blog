from django.db import models  # Importujemy funkcje do tworzenia modeli

class Post(models.Model):  # Tworzymy model "Post", który będzie tabelą w bazie danych
    title = models.CharField(max_length=200)  # Tytuł posta (kolumna w tabeli)
    content = models.TextField()  # Treść posta (kolumna w tabeli)
    published_date = models.DateTimeField(auto_now_add=True)  # Data publikacji (kolumna w tabeli)

    def __str__(self):
        return self.title  # Zwracamy tytuł, kiedy Django wyświetla post

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Komentarz od {self.author} do "{self.post.title}"'
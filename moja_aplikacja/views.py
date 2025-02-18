from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages

# Dodawanie nowego postu
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post został dodany!')  # ✅ KOMUNIKAT
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

# Edytowanie istniejącego postu
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Pobieramy post na podstawie jego ID
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Zapisujemy zmiany
            messages.info(request, 'Post został zaktualizowany!')
            return redirect('post_list')  # Przekierowujemy na stronę główną
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

# Widok listy postów (strona główna)
def post_list(request):
    posts = Post.objects.all()  # Pobieramy wszystkie posty
    return render(request, 'post_list.html', {'posts': posts})

# Widok do usuwania posta
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Pobieramy post lub zwracamy 404
    post.delete()  # Usuwamy post z bazy danych
    messages.warning(request, 'Post został usunięty!')
    return redirect('post_list')  # Przekierowanie na listę postów

# Widok do wyświetlania pojedynczego posta i formularza komentarzy
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Pobieramy wszystkie komentarze powiązane z postem

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Tworzymy komentarz, ale nie zapisujemy jeszcze
            comment.post = post  # Przypisujemy komentarz do posta
            comment.save()  # Zapisujemy do bazy
            return redirect('post_detail', pk=pk)  # Odświeżamy stronę po dodaniu komentarza
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

# TEST KOMUNIKATU
def test_message(request):
    messages.success(request, "To jest testowy komunikat!")  # Dodaj komunikat
    return render(request, 'post_list.html')  # Pokaż w szablonie post_list.html
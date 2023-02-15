from django.shortcuts import render, get_object_or_404
from library.models import Author, Book, Category

def homepage(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    content = {'book':books, 'author':authors, 'category':categories}
    return render(request, 'homepage.html', content)

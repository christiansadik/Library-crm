from django.shortcuts import render, get_object_or_404
from library.models import Author, Book, Category

def homepage(request):
    books = Book.objects.all()
    content = {'books':books}
    return render(request, 'homepage.html', content)

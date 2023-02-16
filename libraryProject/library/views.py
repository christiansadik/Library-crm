from django.shortcuts import render, get_object_or_404
from .models import Author
# Create your views here.


def author(request, id):
    author = get_object_or_404(Author, id=id)
    content = {'author':author}
    return render (request, 'author.html', content)
from django.shortcuts import render, get_object_or_404
from library.models import Author, Book, Category

# Import Class Based Views Api
from django.views.generic.list import ListView

# With function
# def homepage(request):
#     books = Book.objects.all()
#     content = {'books':books}
#     return render(request, 'homepage.html', content)

# With Class -> ListView
class BookListViews(ListView):
    model = Book
    template_name = 'homepage.html'







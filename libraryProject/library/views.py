from django.shortcuts import render, get_object_or_404
from .models import Author
# Create your views here.

from django.views.generic.detail import DetailView

# With function
# def author(request, id):
#     author = get_object_or_404(Author, id=id)
#     content = {'author':author}
#     return render (request, 'author.html', content)

# With Detail List View Class
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author.html'

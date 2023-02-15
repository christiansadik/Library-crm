from django.db import models
from django.urls import reverse

# Create your models here.
'''
LIBRO: titolo, autore, genere, isbn

AUTORE: nome, cognome, azione

GENERE: nome
'''

class Author(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

    def __str__(self) -> str:
        return self.name + ' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse('author', kwargs ={'id':self.id})

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'

    def __str__(self) -> str:
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories =models.ManyToManyField(Category)
    isbn = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'

    def __str__(self) -> str:
        return self.title
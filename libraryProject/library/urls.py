from django.urls import path

from .views import AuthorDetailView # author

urlpatterns = [
    # path('author/<int:id>', author,  name='author')
    path('author/<int:pk>/', AuthorDetailView.as_view(),  name='author')
]
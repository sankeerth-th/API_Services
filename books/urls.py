from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('titles/', views.TitleListView.as_view(), name='title-list'),
]
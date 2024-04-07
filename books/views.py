from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Author, Title
import logging

logger = logging.getLogger(__name__)

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        logger.info("Fetching all books for BookListView")
        return super().get_queryset()

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        logger.info("Fetching all authors for AuthorListView")
        return super().get_queryset()

class TitleListView(ListView):
    model = Title
    template_name = 'title_list.html'
    context_object_name = 'titles'

    def get_queryset(self):
        logger.info("Fetching all titles for TitleListView")
        return super().get_queryset()

def home_view(request):
    logger.info("Rendering the homepage with lists of books, authors, and titles.")
    try:
        books = Book.objects.all()
        authors = Author.objects.all()
        titles = Title.objects.all()
        context = {
            'books': books,
            'authors': authors,
            'titles': titles,
        }
        return render(request, 'API_Service/home.html', context)
    except Exception as e:
        logger.error("Error rendering the homepage with lists: %s", e, exc_info=True)
        return render(request, 'API_Service/error.html', {'error': 'Error loading the page'})
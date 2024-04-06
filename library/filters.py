import django_filters
from .models import Book
import logging

# Configure logger
logger = logging.getLogger(__name__)

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author__id')
    publication_year = django_filters.NumberFilter()
    genre = django_filters.NumberFilter(field_name='genre__id')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre']

    def __init__(self, *args, **kwargs):
        super(BookFilter, self).__init__(*args, **kwargs)
        logger.info("BookFilter initialized with filters for title, author, publication_year, and genre.")

    def filter_queryset(self, queryset):
        try:
            filtered_queryset = super(BookFilter, self).filter_queryset(queryset)
            logger.info("Book queryset filtered successfully.")
            return filtered_queryset
        except Exception as e:
            logger.error("Error filtering book queryset: %s", e, exc_info=True)
            raise
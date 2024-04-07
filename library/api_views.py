from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .throttles import ReadRateThrottle, WriteRateThrottle
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger(__name__)

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [ReadRateThrottle, WriteRateThrottle]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error fetching authors: %s", e, exc_info=True)
            return Response({"error": "Error fetching authors"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error creating author: %s", e, exc_info=True)
            return Response({"error": "Error creating author"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    throttle_classes = [ReadRateThrottle, WriteRateThrottle]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error fetching author detail: %s", e, exc_info=True)
            return Response({"error": "Error fetching author detail"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error updating author: %s", e, exc_info=True)
            return Response({"error": "Error updating author"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error deleting author: %s", e, exc_info=True)
            return Response({"error": "Error deleting author"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [ReadRateThrottle, WriteRateThrottle]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error fetching books: %s", e, exc_info=True)
            return Response({"error": "Error fetching books"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error creating book: %s", e, exc_info=True)
            return Response({"error": "Error creating book"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [ReadRateThrottle, WriteRateThrottle]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error fetching book detail: %s", e, exc_info=True)
            return Response({"error": "Error fetching book detail"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error updating book: %s", e, exc_info=True)
            return Response({"error": "Error updating book"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error deleting book: %s", e, exc_info=True)
            return Response({"error": "Error deleting book"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
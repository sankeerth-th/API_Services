from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateUserView
import logging

# Configure logger
logger = logging.getLogger(__name__)

urlpatterns = []

try:
    urlpatterns += [
        path('authors/', api_views.AuthorList.as_view(), name='author-list'),
        path('authors/<int:pk>/', api_views.AuthorDetail.as_view(), name='author-detail'),
        path('books/', api_views.BookList.as_view(), name='book-list'),
        path('books/<int:pk>/', api_views.BookDetail.as_view(), name='book-detail'),
        path('genres/', api_views.GenreList.as_view(), name='genre-list'),
        path('genres/<int:pk>/', api_views.GenreDetail.as_view(), name='genre-detail'),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('register/', CreateUserView.as_view(), name='create_user'),
    ]
    logger.info("URL patterns for library app successfully configured.")
except Exception as e:
    logger.error("Error configuring URL patterns for library app: %s", e, exc_info=True)
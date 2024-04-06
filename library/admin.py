from django.contrib import admin
from .models import Author, Genre, Book
import logging

# Configure logger
logger = logging.getLogger(__name__)

try:
    admin.site.register(Author)
    admin.site.register(Genre)
    admin.site.register(Book)
    logger.info("Models registered successfully in admin.")
except Exception as e:
    logger.error("Error registering models in admin: %s", e, exc_info=True)
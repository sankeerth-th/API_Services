from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import logging

logger = logging.getLogger(__name__)

class Author(models.Model):
    name = models.CharField(_("name"), max_length=255)
    bio = models.TextField(_("bio"), blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(_("title"), max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(_("description"), blank=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Log book creation
        logger.info(f"Book '{self.title}' by {self.author.name} saved.")

class Title(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='titles')
    title = models.CharField(_("title"), max_length=255)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            # Log title creation
            logger.info(f"Title '{self.title}' for book '{self.book.title}' saved.")
        except Exception as e:
            logger.error(f"Error saving title: {e}")
            raise e
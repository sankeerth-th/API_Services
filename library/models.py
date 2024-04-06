from django.db import models
import logging

# Configure logger
logger = logging.getLogger(__name__)

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info(f"Author '{self.name}' saved successfully.")
        except Exception as e:
            logger.error("Error saving Author: %s", e, exc_info=True)
            raise

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info(f"Genre '{self.name}' saved successfully.")
        except Exception as e:
            logger.error("Error saving Genre: %s", e, exc_info=True)
            raise

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            logger.info(f"Book '{self.title}' saved successfully.")
        except Exception as e:
            logger.error("Error saving Book: %s", e, exc_info=True)
            raise
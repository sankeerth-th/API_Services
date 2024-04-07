from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import logging

logger = logging.getLogger(__name__)

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(_("bio"), blank=True)
    website_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Log post creation
        logger.info(f"Post '{self.title}' by {self.author.username} saved.")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            # Log comment creation
            logger.info(f"Comment on '{self.post.title}' by {self.author.username} saved.")
        except Exception as e:
            logger.error(f"Error saving comment: {e}")  # Log the entire error message and trace
            raise e  # Reraise the exception to ensure it's not swallowed
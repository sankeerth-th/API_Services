from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author, Book, Genre
import logging

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            logger.info("User created successfully.")
            return user
        except Exception as e:
            logger.error("Error creating user: %s", e, exc_info=True)
            raise

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'genre']

    def create(self, validated_data):
        try:
            genres_data = validated_data.pop('genre')
            book = Book.objects.create(**validated_data)
            book.genre.set(genres_data)
            book.save()
            logger.info(f"Book '{book.title}' created successfully.")
            return book
        except Exception as e:
            logger.error("Error creating Book instance: %s", e, exc_info=True)
            raise

    def update(self, instance, validated_data):
        try:
            genres_data = validated_data.pop('genre', None)
            if genres_data is not None:
                instance.genre.set(genres_data)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            logger.info(f"Book '{instance.title}' updated successfully.")
            return instance
        except Exception as e:
            logger.error("Error updating Book instance: %s", e, exc_info=True)
            raise
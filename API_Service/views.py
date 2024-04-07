from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from library.models import Book, Author, Genre  # Corrected import to use 'library' app models
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def home_view(request):
    """Render the homepage with lists of books, authors, and genres."""
    logger.info("Rendering the homepage with lists of books, authors, and genres.")
    try:
        books = Book.objects.all()
        authors = Author.objects.all()
        genres = Genre.objects.all()  # Updated to use Genre instead of Title
        context = {
            'books': books,
            'authors': authors,
            'genres': genres,  # Updated context to include genres
        }
        return render(request, 'API_Service/home.html', context)
    except Exception as e:
        logger.error("Error rendering the homepage with lists: %s", e, exc_info=True)
        return HttpResponse(status=500)

def login_view(request):
    """Handle the login functionality."""
    logger.info("Attempting login.")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'API_Service/login.html', {'form': form})

def logout_view(request):
    """Handle the logout functionality."""
    logger.info("Logging out.")
    try:
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('home')
    except Exception as e:
        logger.error("Logout error: %s", e, exc_info=True)
        return HttpResponse(status=500)
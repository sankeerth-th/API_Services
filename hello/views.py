from django.http import HttpResponse
import logging

# Configure logger
logger = logging.getLogger(__name__)

def hello_world(request):
    try:
        logger.info("Serving the 'Hello, World!' page.")
        return HttpResponse("Hello, World!")
    except Exception as e:
        logger.error("Error serving the 'Hello, World!' page: %s", e, exc_info=True)
        return HttpResponse("An error occurred.", status=500)
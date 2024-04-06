from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
import logging

# Configure logger
logger = logging.getLogger(__name__)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            logger.info("Attempting user registration.")
            return super().post(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error during user registration: %s", e, exc_info=True)
            return Response({"error": "User registration failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
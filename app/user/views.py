from user.serializers import UserSerializer
from rest_framework import generics

class CreateUserAPi(generics.CreateAPIView):
    """Create a new user in system"""
    serializer_class = UserSerializer
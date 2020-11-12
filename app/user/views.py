from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new uath token for user"""
    serializer_class = AuthTokenSerializer
    #renderer class helps us to make the post request through the browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

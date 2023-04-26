from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


# for ability having separated classes for creating/updating User. Cause we use generics, not viewsets

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Retrieve/Patch/Update
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # access to this view if only authenticated
    # In headers must be Header-authorisation & valid token
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Necessary for getting information only for authorisated user - just write "me", without id
    # http://127.0.0.1:8000/api/user/me/
    def get_object(self):
        return self.request.user

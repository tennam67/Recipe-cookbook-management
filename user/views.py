from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from user.serializers import UserCreationSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserCreationSerializer
    permission_classes = []
    # empty square bracket: you can't be authenticated
    # because default permission in the config settings  is authenticated


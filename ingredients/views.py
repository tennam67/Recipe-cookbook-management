from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class GetCreateIngredientView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GetUpdateDeleteIngredientView(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

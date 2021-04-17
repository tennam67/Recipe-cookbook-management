from django.shortcuts import render

# Create your views here.
from rest_framework import status, filters

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


#
# class GetRecipeView(GenericAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#
#     # (RecipeSerializer) this one you can give any name
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class CreateRecipeView(GenericAPIView):
#     serializer_class = RecipeSerializer
#
#     # (RecipeSerializer) this one you can give any name
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # will the requirements
#         serializer.save()
#         # creating instance
#         return Response(serializer.data)

class GetCreateRecipeView(GenericAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # (RecipeSerializer) this one you can give any name

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # will the requirements
        serializer.save()
        # creating instance
        return Response(serializer.data)


class GetUpdateDeleteRecipeView(GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

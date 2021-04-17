# from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cookbook.models import CookBook
# from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
# from rest_framework.response import Response
from cookbook.permissions import IsAuthorOrAdmin
from cookbook.serializers import CookBookSerializer


# list queryset - for logged user
class GetAuthorCookBookView(ListCreateAPIView):
    serializer_class = CookBookSerializer
    lookup_url_kwarg = "user_id"
    lookup_field = "author"

    def get_queryset(self):
        return CookBook.objects.filter(author=self.request.user)


class GetCreateBookView(ListCreateAPIView):
    queryset = CookBook.objects.all()
    serializer_class = CookBookSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        # self.request because request is going to be it's own instance


class GetUpdateDeleteBookView(RetrieveUpdateDestroyAPIView):
    # This will overrides the default authentication
    permission_classes = [IsAuthorOrAdmin]
    queryset = CookBook.objects.all()
    serializer_class = CookBookSerializer
    lookup_url_kwarg = "book_id"
    lookup_field = "id"


# default behaviour is pk and we changed it to id

class SearchCookBookView(ListAPIView):
    serializer_class = CookBookSerializer

    def get_queryset(self):
        return CookBook.objects.filter(title__icontains=self.kwargs["ref"])


# class GetCreateBookView(GenericAPIView):
#     queryset = CookBook.objects.all()
#     serializer_class = CookBookSerializer
#
#     # (RecipeSerializer) this one you can give any name
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # will the requirements
#         serializer.save(author=request.user)
#         # creating instance
#         return Response(serializer.data)


# class GetUpdateDeleteBookView(GenericAPIView):
#     queryset = CookBook.objects.all()
#     serializer_class = CookBookSerializer
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

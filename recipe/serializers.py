from rest_framework import serializers

from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
        # we want all the fields to be serialized

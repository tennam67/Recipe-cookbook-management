from rest_framework import serializers

from ingredients.serializers import IngredientSerializer
from recipe.models import Recipe


# class RecipeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = "__all__"
#         # we want all the fields to be serialized

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    # def validate(self, data):
    #     if not len(data.get("ingredients")):
    #         raise serializers.ValidationError(" Don't leave the ingredients empty")
    #     return data

    class Meta:
        model = Recipe
        fields = "__all__"
        read_only_fields = ["ingredients"]
        # fields = ["id", "title", "description", "ingredients"]
        # we want all the fields to be serialized

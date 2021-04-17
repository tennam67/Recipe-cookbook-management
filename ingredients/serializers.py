from rest_framework import serializers

from ingredients.models import Ingredient
from user.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    # def validate(self, data):
    #     if not len(data.get("ingredients")):
    #         raise serializers.ValidationError(" Don't leave the ingredients empty")
    #     return data

    class Meta:
        model = Ingredient
        # fields = ["id", "name", "description", "favourite", "author"]
        fields = "__all__"
        read_only_fields = ["author"]
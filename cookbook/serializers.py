from rest_framework import serializers

from cookbook.models import CookBook
from recipe.serializers import RecipeSerializer
from user.serializers import UserSerializer


class CookBookSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    recipe = RecipeSerializer(many=True)


    total_recipes = serializers.SerializerMethodField()

# this mehtod should start with get_ and add the field name ( eg: get_get_total_recipes )
    def get_total_recipes(self, instance):
        return len(instance.recipe.all())

    class Meta:
        model = CookBook
        fields = "__all__"
        read_only_fields = ["author"]
        # we want all the fields to be serialized

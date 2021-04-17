from rest_framework import serializers

from cookbook.models import CookBook


class CookBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookBook
        fields = "__all__"
        read_only_fields = ["author"]
        # we want all the fields to be serialized

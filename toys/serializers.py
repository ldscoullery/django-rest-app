from rest_framework import serializers
from toys.models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy # the model related to the serializer
        fields = ('id',  # the field names that we want to include in the serialization from related model
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_included_in_home')

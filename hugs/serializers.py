from django.db import IntegrityError
from rest_framework import serializers
from hugs.models import Hug


class HugSerializer(serializers.ModelSerializer):
    """
    Serializer for the Hug model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Hug
        fields = ['id', 'created_at', 'owner', 'hug']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail' : 'possible duplicate'
            })
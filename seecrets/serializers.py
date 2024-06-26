from rest_framework import serializers
from .models import Seecret
from hugs.models import Hug


class SeecretSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    hug_id = serializers.SerializerMethodField()
    hugs_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_hug_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            hug = Hug.objects.filter(
                owner=user, hug=obj
            ).first()
            return hug.id if hug else None
        return None

    class Meta:
        model = Seecret
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter', 'hug_id',
            'hugs_count', 'comments_count',
        ]

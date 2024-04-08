from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Reach_out


class Reach_outSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reach_out model
    Adds three extra fields when returning a list of Reach_out instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Reach_out
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'created_at', 
            'updated_at', 'reach_out_content', 'reach_out_to'
        ]

class Reach_outDetailSerializer(Reach_outSerializer):
    """
    Serializer for the Comment model used in Detail view
    Profile is a read only field so that we dont have to set it on each update
    """
    reach_out_to = serializers.ReadOnlyField(source='profile.id')
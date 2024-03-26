from rest_framework import serializers
from .models import Reach_out


class Reach_outSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reach_out model
    Adds three extra fields when returning a list of Reach_out instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    reach_out_id = serializers.ReadOnlyField(source='owner.profile.id')
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Reach_out
        fields = [
           'owner', 'is_owner', 'reach_out_id',
            'reach_out_to', 'created_at', 'updated_at', 'reach_out_content'
        ]

class Reach_outDetailSerializer(Reach_outSerializer):
    """
    Serializer for the Reach_out model used in Detail view
    Reach_out is a read only field so that we dont have to set it on each update
    """
    reach_out_id = serializers.ReadOnlyField(source='reach_out.id')
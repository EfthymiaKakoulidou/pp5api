from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Reach_out
from .serializers import Reach_outSerializer, Reach_outDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly, IsReachOutToProfile, IsOwner

class Reach_outList(generics.ListCreateAPIView):
    serializer_class = Reach_outSerializer
    permission_classes = [IsAuthenticated, IsOwner, IsReachOutToProfile]

    def get_queryset(self):
        user = self.request.user
        return Reach_out.objects.filter(owner=user) | Reach_out.objects.filter(reach_out_to=user.profile)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Reach_outDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner, IsReachOutToProfile]
    serializer_class = Reach_outDetailSerializer
    def get_queryset(self):
        # Get the authenticated user
        user = self.request.user

        # Filter queryset to include objects where either the owner or the reach_out_to profile matches the authenticated user
        queryset = Reach_out.objects.filter(
            Q(owner=user) | Q(reach_out_to=user.profile)
        )
        
        return queryset
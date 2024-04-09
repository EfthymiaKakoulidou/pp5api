from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsReachOutToProfile, IsOwner
from .models import Reach_out
from .serializers import Reach_outSerializer, Reach_outDetailSerializer


class Reach_outList(generics.ListCreateAPIView):
    serializer_class = Reach_outSerializer
    permission_classes = [IsAuthenticated, IsOwner, IsReachOutToProfile]

    def get_queryset(self):
        return Reach_out.objects.filter(reach_out_to=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Reach_outDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner, IsReachOutToProfile]
    serializer_class = Reach_outDetailSerializer
    queryset = Reach_out.objects.all()
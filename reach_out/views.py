from rest_framework import generics, permissions
from drf_api.permissions import IsReachOutToProfile
from .models import Reach_out
from .serializers import Reach_outSerializer, Reach_outDetailSerializer


class Reach_outList(generics.ListCreateAPIView):
    serializer_class = Reach_outSerializer
    permission_classes = [IsReachOutToProfile]

    def get_queryset(self):
        return Reach_out.objects.filter(reach_out_to=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Reach_outDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReachOutToProfile]
    serializer_class = Reach_outDetailSerializer
    queryset = Reach_out.objects.all()
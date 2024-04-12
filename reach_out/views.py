from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Reach_out
from .serializers import Reach_outSerializer, Reach_outDetailSerializer
from drf_api.permissions import IsOwnerOrReadOnly, IsReachOutToProfile

class Reach_outList(generics.ListCreateAPIView):
    serializer_class = Reach_outSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Reach_out.objects.filter(owner=user) | Reach_out.objects.filter(reach_out_to=user.profile)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Reach_outDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsReachOutToProfile]
    serializer_class = Reach_outDetailSerializer
    queryset = Reach_out.objects.all()
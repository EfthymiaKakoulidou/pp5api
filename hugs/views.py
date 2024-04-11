from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from hugs.models import Hug
from .serializers import HugSerializer


class HugList(generics.ListCreateAPIView):
    serializer_class = HugSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hug.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HugDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a hug or delete it by id if you own it.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = HugSerializer
    queryset = Hug.objects.all()
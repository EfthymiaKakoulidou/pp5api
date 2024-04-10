from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Reach_out_comment
from .serializers import Reach_out_commentSerializer, Reach_out_commentDetailSerializer


class Reach_out_commentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = Reach_out_commentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reach_out_comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reach_out']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Reach_out_commentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = Reach_out_commentDetailSerializer
    queryset = Reach_out_comment.objects.all()
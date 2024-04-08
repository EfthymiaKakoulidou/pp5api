from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Seecret
from .serializers import SeecretSerializer


class SeecretList(generics.ListCreateAPIView):
    """
    List secrets or create a post if logged in
    The perform_create method associates the secret with the logged in user.
    """
    serializer_class = SeecretSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Seecret.objects.annotate(
        hugs_count=Count('hugs', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        
        'hugs__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'hugs_count',
        'comments_count',
        'hugs__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SeecretDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a seecret and edit or delete it if you own it.
    """
    serializer_class = SeecretSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Seecret.objects.annotate(
        hugs_count=Count('hugs', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
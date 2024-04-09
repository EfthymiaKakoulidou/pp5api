from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly, IsOwner
from .models import Diary
from .serializers import DiarySerializer

class DiaryList(generics.ListCreateAPIView):
    """
    List diary entries displayed just on the diary
    The perform_create method associates the entry with the logged in user.
    """
    serializer_class = DiarySerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Diary.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a diary entry and edit or delete it if you own it.
    """
    serializer_class = DiarySerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Diary.objects.filter(owner=self.request.user)
    

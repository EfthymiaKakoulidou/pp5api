from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly, IsOwner, IsSuperuserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer


class BlogList(generics.ListCreateAPIView):
    """
    List blogposts or create a blog if superuser
    The perform_create method associates the secret with the logged in user.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a blogpost and edit or delete it if you are superuser.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrReadOnly]
    queryset = Blog.objects.all()


    

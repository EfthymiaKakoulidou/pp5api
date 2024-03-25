from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Seecret
from .serializers import SeecretSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class SeecretList(APIView):
    serializer_class = SeecretSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        seecrets = Seecret.objects.all()
        serializer = SeecretSerializer(
            seecrets, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = SeecretSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class SeecretDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SeecretSerializer

    def get_object(self, pk):
        try:
            seecret = Seecret.objects.get(pk=pk)
            self.check_object_permissions(self.request, seecret)
            return seecret
        except Seecret.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seecret = self.get_object(pk)
        serializer = SeecretSerializer(
            seecret, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        seecret = self.get_object(pk)
        serializer = SeecretSerializer(
            seecret, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        seecret = self.get_object(pk)
        seecret.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Seecret
from .serializers import SeecretSerializer


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
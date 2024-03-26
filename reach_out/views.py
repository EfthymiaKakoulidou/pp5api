from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly, IsProfileOwner
from .models import Reach_out
from .serializers import Reach_outSerializer, Reach_outDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Profile


class Reach_outList(APIView):
    """
    List all reach_outs
    No Create view (post method), as reach_out creation handled by django signals
    """
    def get(self, request):
        reach_outs = Reach_out.objects.all()
        serializer = Reach_outSerializer(
            reach_outs, many=True, context={'request': request
            })
        return Response(serializer.data)


class Reach_outDetail(APIView):
    serializer_class = Reach_outSerializer
    permission_classes = [IsProfileOwner]
    def get_object(self,pk):
        try:
            reach_out = Reach_out.objects.get(pk=pk)
            self.check_object_permissions(self.request, reach_out)
            return reach_out
        except Reach_out.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        reach_out = self.get_object(pk)
        serializer = Reach_outSerializer(
            reach_out, context={'request': request
            })
        return Response(serializer.data)

    def put(self, request, pk):
        reach_out = self.get_object(pk)
        serializer = ProfileSerializer(
            reach_out, data=request.data, context={'request': request
            })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
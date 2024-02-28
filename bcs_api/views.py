from rest_framework.views import APIView
from bcs.models import BcsData
from .serializers import BcsDataSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST


class ImportView(APIView):
    def post(self, request, format=None):
        serializer = BcsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('ok', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

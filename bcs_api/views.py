from rest_framework import generics
from bcs.models import BcsData
from .serializers import BcsDataSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class ImportView(generics.CreateAPIView):
    queryset = BcsData.objects.all()
    serializer_class = BcsDataSerializer


class ApiLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

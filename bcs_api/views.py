from rest_framework import generics
from bcs.models import BcsData
from .serializers import BcsDataSerializer


class ImportView(generics.CreateAPIView):
    queryset = BcsData.objects.all()
    serializer_class = BcsDataSerializer

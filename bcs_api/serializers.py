from rest_framework import serializers
from bcs.models import BcsData


class BcsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BcsData
        fields = ['id', 'cow', 'score']

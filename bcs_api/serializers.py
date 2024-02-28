from rest_framework import serializers
from bcs.models import BcsData, Cow
from django.utils import timezone


class BcsDataSerializer(serializers.ModelSerializer):
    main = serializers.ListField(child=serializers.DictField())

    class Meta:
        model = BcsData
        fields = ['main']

    def create(self, validated_data):

        validated_data = validated_data.get('main')
        if not validated_data:
            return []

        today = timezone.now().date()
        filtered_bcs_data = BcsData.objects.filter(create_date__date=today)
        filtered_bcs_data.delete()

        bcs_data_list = []
        for item in validated_data:
            cow_code = item.pop('id')
            cow = Cow.objects.get(code=cow_code)
            bcs_data = BcsData.objects.create(cow=cow, score=item['score'])
            bcs_data_list.append(bcs_data)
        return bcs_data_list

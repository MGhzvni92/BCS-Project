from rest_framework import serializers
from bcs.models import BcsData, Cow


class BcsDataSerializer(serializers.ModelSerializer):
    main = serializers.ListField(child=serializers.DictField())

    class Meta:
        model = BcsData
        fields = ['main']

    def create(self, validated_data):
        bcs_data_list = []
        for item in validated_data['main']:
            cow_code = item.pop('id')
            bcs_data = BcsData.objects.create(cow_code=cow_code, **item)
            bcs_data_list.append(bcs_data)
        return bcs_data_list
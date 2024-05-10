from rest_framework import serializers
from .models import Column_mapping_data,MappingData

class column_serializer(serializers.ModelSerializer):
    class Meta:
        model = Column_mapping_data
        fields = '__all__'

class post_mapping_serializer(serializers.ModelSerializer):
    class Meta:
        model = MappingData
        fields = '__all__'

class get_mapping_serializer(serializers.ModelSerializer):
    class Meta:
        model = MappingData
        fields = '__all__'
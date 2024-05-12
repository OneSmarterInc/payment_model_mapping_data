from rest_framework import serializers
from .models import Column_mapping_data,MappingData,company_onbording_payment,sub_company_onbording_payment,vendor_onbording_payment,ban_onboarding_payment

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

class company_onbording_payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = company_onbording_payment
        fields = '__all__'

class sub_company_onbording_payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = sub_company_onbording_payment
        fields = '__all__'

class vendor_onbording_payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_onbording_payment
        fields = "__all__"

class ban_onbording_payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = ban_onboarding_payment
        fields = "__all__"
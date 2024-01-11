
from rest_framework import serializers
from Vendors.models import Vendor
from django.contrib.auth.models import User

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = [
            'id', 'vendor_code', 'user',             
            'on_time_delivery_rate', 'quality_rating_avg',
            'average_response_time', 'fulfillment_rate',
        ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

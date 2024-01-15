
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from Vendors.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = [
            'id', 'vendor_code', 'user',             
            'on_time_delivery_rate', 'quality_rating_avg',
            'average_response_time', 'fulfillment_rate',
        ]

    def validate_contact_details(self, value):
        if len(value) not in [10, 12]:
            raise serializers.ValidationError('Contact details must be either 10 or 12 characters long.')

        if not value.isdigit():
            raise serializers.ValidationError('Contact details must contain only numeric characters.')

        return value

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


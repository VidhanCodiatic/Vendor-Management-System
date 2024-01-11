
from Vendors.models import Vendor
from Vendors.serializers import VendorSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from Vendors.permissions import UserPermission



class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [UserPermission]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if Vendor.objects.filter(user=user).exists():
            return Response({'error': 'User already has a Vendor.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                serializer.validated_data['user'] = user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error' : str(e)})
        
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]



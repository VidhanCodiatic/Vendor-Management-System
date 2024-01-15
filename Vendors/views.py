
from django.contrib.auth.models import User
from rest_framework import status, viewsets, generics
from rest_framework.response import Response

from Vendors.models import Vendor
from Vendors.permissions import VendorPermission
from Vendors.serializers import UserSerializer, VendorSerializer


class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [VendorPermission]

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
        
class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

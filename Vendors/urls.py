from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Vendors.views import UserAPIView, VendorModelViewSet

vendorRouter = DefaultRouter()
vendorRouter.register('vendors', VendorModelViewSet, basename='vendors')
# vendorRouter.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(vendorRouter.urls)),
    path('users/', UserAPIView.as_view(), name='users')
]
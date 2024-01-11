from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Vendors.views import VendorModelViewSet, UserModelViewSet

vendorRouter = DefaultRouter()
vendorRouter.register('vendors', VendorModelViewSet, basename='vendors')
vendorRouter.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    path('', include(vendorRouter.urls)), #for userRouter urls
]
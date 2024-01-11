from django.urls import include, path
from rest_framework.routers import DefaultRouter

from PurchaseOrders.views import PurchaseOrderModelViewSet

orderRouter = DefaultRouter()
orderRouter.register('purchase_orders', PurchaseOrderModelViewSet, basename='purchase_orders')

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')), # for user's login and logout
    path('', include(orderRouter.urls)), #for userRouter urls
]
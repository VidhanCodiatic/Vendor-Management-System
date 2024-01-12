from django.urls import include, path
from rest_framework.routers import DefaultRouter

from PurchaseOrders.views import PurchaseOrderModelViewSet

orderRouter = DefaultRouter()
orderRouter.register('purchase_orders', PurchaseOrderModelViewSet, basename='purchase_orders')

urlpatterns = [
    path('', include(orderRouter.urls)),
]
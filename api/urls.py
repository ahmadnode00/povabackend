from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet, basename='shipment')

urlpatterns = [
    # Short, friendly tracking endpoint
    path('track/<str:tracking_number>/', ShipmentViewSet.as_view({'get': 'retrieve'}), name='track'),

    # Include standard router endpoints
    path('', include(router.urls)),
]

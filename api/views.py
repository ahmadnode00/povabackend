from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Shipment, ShipmentImage
from .serializers import ShipmentSerializer, ShipmentImageSerializer
from datetime import datetime
import json


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    lookup_field = 'tracking_number'

    @action(detail=True, methods=['get'])
    def by_tracking(self, request, tracking_number=None):
        """
        GET /api/shipments/<tracking_number>/
        Returns full shipment info with coordinates and images.
        """
        shipment = get_object_or_404(Shipment, tracking_number=tracking_number)
        serializer = ShipmentSerializer(shipment)
        data = serializer.data

        # Add image URLs
        data['images'] = [img.image.url for img in shipment.images.all()]

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """
        GET /api/shipments/<tracking_number>/
        Routes retrieval through by_tracking()
        """
        tracking_number = self.kwargs.get('tracking_number')
        if tracking_number:
            return self.by_tracking(request, tracking_number)
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def update_location(self, request, tracking_number=None):
        """
        POST /api/shipments/<tracking_number>/update_location/
        Updates current location ONLY (no timeline).
        """
        shipment = get_object_or_404(Shipment, tracking_number=tracking_number)

        current_lat = request.data.get('current_lat')
        current_lng = request.data.get('current_lng')
        location_name = request.data.get('location_name', 'Unknown Location')
        status_update = request.data.get('status', shipment.status)

        if current_lat is None or current_lng is None:
            return Response(
                {'error': 'current_lat and current_lng are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update shipment fields
        shipment.current_lat = current_lat
        shipment.current_lng = current_lng
        shipment.current_location = location_name
        shipment.status = status_update

        shipment.save()

        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def images(self, request, tracking_number=None):
        """
        GET /api/shipments/<tracking_number>/images/
        Returns all images for this shipment.
        """
        shipment = get_object_or_404(Shipment, tracking_number=tracking_number)
        images = shipment.images.all()
        serializer = ShipmentImageSerializer(images, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload_image(self, request, tracking_number=None):
        """
        POST /api/shipments/<tracking_number>/upload_image/
        Upload one or multiple shipment images.
        """
        shipment = get_object_or_404(Shipment, tracking_number=tracking_number)

        files = request.FILES.getlist('images') or (
            [request.FILES.get('image')] if request.FILES.get('image') else []
        )

        created = []
        for f in files:
            if not f:
                continue
            created.append(
                ShipmentImage.objects.create(
                    shipment=shipment,
                    image=f,
                    caption=request.data.get('caption', '')
                )
            )

        serializer = ShipmentImageSerializer(created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def list_all(self, request):
        """
        GET /api/shipments/list/
        Returns all shipments with optional filters.
        """
        queryset = self.get_queryset()

        status_filter = request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        shipper_country = request.query_params.get('shipper_country')
        if shipper_country:
            queryset = queryset.filter(shipper_country=shipper_country)

        receiver_country = request.query_params.get('receiver_country')
        if receiver_country:
            queryset = queryset.filter(receiver_country=receiver_country)

        serializer = ShipmentSerializer(queryset, many=True)
        return Response(serializer.data)

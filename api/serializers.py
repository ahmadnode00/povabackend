from rest_framework import serializers
from .models import Shipment, ShipmentImage
import json


class ShipmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentImage
        fields = ["id", "shipment", "image", "caption", "uploaded_at"]


class ShipmentSerializer(serializers.ModelSerializer):
    # Parse timeline JSON for frontend
    shipment_progress = serializers.SerializerMethodField()
    
    # Return coordinates as [lat, lng] arrays
    pickup = serializers.SerializerMethodField()
    dropoff = serializers.SerializerMethodField()
    current_location_coords = serializers.SerializerMethodField()
    
    # Include related images
    images = ShipmentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shipment
        fields = [
            "id",
            "tracking_number",
            "package_type",
            "package_description",
            "departure_datetime",
            "expected_arrival_datetime",
            
            # Locations (text)
            "origin_city",
            "destination_city",
            "delivery_address",
            "transit_point",
            "current_location",
            
            # Shipper
            "shipper_full_name",
            "shipper_email",
            "shipper_country",
            "shipper_city",
            "shipper_address",
            
            # Receiver
            "receiver_full_name",
            "receiver_email",
            "receiver_country",
            "receiver_city",
            "receiver_address",
            
            # Pricing
            "price",
            "shipment_price",
            "weight",
            "amount_due",
            
            # Status
            "status",
            
            # Coordinates
            "pickup_lat",
            "pickup_lng",
            "dropoff_lat",
            "dropoff_lng",
            "current_lat",
            "current_lng",
            "pickup",
            "dropoff",
            "current_location_coords",
            
            # Timeline & Images
            "shipment_progress",
            "images",
            
            "created_at",
            "updated_at",
        ]

   
    def get_pickup(self, obj):
        """Return pickup as [lat, lng]"""
        if obj.pickup_lat and obj.pickup_lng:
            return [float(obj.pickup_lat), float(obj.pickup_lng)]
        return None

    def get_dropoff(self, obj):
        """Return dropoff as [lat, lng]"""
        if obj.dropoff_lat and obj.dropoff_lng:
            return [float(obj.dropoff_lat), float(obj.dropoff_lng)]
        return None

    def get_current_location_coords(self, obj):
        """Return current location as [lat, lng]"""
        if obj.current_lat and obj.current_lng:
            return [float(obj.current_lat), float(obj.current_lng)]
        return None

    def get_shipment_progress(self, obj):
        """Parse shipment_progress JSON string to list"""
        if obj.shipment_progress:
            try:
                return json.loads(obj.shipment_progress)
            except (json.JSONDecodeError, TypeError):
                return []
        return []

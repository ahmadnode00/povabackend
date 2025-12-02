from django.contrib import admin
from .models import Shipment, ShipmentImage


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'status', 'shipper_full_name', 'receiver_full_name', 'created_at')
    search_fields = ('tracking_number', 'shipper_full_name', 'receiver_full_name', 'shipper_email', 'receiver_email')
    list_filter = ('status', 'shipper_country', 'receiver_country')


@admin.register(ShipmentImage)
class ShipmentImageAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'caption', 'uploaded_at')
    search_fields = ('shipment__tracking_number', 'caption')

from django.db import models


class Shipment(models.Model):
    # Auto-increment primary key (keeps DRF's `id` field available)
    id = models.BigAutoField(primary_key=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    # Tracking & Basic Info
    tracking_number = models.CharField(max_length=100, unique=True)
    package_type = models.CharField(max_length=100, blank=True)
    package_description = models.TextField(blank=True)
    
    # Dates
    departure_datetime = models.DateTimeField(null=True, blank=True)
    expected_arrival_datetime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Locations (Text)
    origin_city = models.CharField(max_length=100, blank=True)
    destination_city = models.CharField(max_length=100, blank=True)
    delivery_address = models.TextField(blank=True)
    transit_point = models.CharField(max_length=100, blank=True)
    current_location = models.CharField(max_length=100, blank=True)
    
    # Shipper Information
    shipper_full_name = models.CharField(max_length=200, blank=True)
    shipper_email = models.EmailField(blank=True)
    shipper_country = models.CharField(max_length=100, blank=True)
    shipper_city = models.CharField(max_length=100, blank=True)
    shipper_address = models.TextField(blank=True)
    
    # Receiver Information
    receiver_full_name = models.CharField(max_length=200, blank=True)
    receiver_email = models.EmailField(blank=True)
    receiver_country = models.CharField(max_length=100, blank=True)
    receiver_city = models.CharField(max_length=100, blank=True)
    receiver_address = models.TextField(blank=True)
    
    # Pricing & Weight
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # Coordinates (Pickup, Dropoff, Current)
    pickup_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pickup_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    dropoff_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    dropoff_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Timeline (JSON stored as text)
    shipment_progress = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Shipment {self.tracking_number}"


class ShipmentImage(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='shipment_images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"Image for {self.shipment.tracking_number}"

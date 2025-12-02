#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Shipment

# Fix the tracking number with wrong longitude signs
s = Shipment.objects.get(tracking_number='US-EXP-95837265')
s.pickup_lng = -74.170020
s.dropoff_lng = -112.010620
s.current_lng = -83.070320
s.save()

print(f'✓ Fixed US-EXP-95837265')
print(f'  Pickup: ({s.pickup_lat}, {s.pickup_lng})')
print(f'  Dropoff: ({s.dropoff_lat}, {s.dropoff_lng})')
print(f'  Current: ({s.current_lat}, {s.current_lng})')

# Also check and fix US-EXP-95837266 if it has the same issue
try:
    s2 = Shipment.objects.get(tracking_number='US-EXP-95837266')
    if s2.pickup_lng and s2.pickup_lng > 0:
        s2.pickup_lng = -74.170020
        s2.dropoff_lng = -112.010620
        s2.current_lng = -83.070320
        s2.save()
        print(f'✓ Fixed US-EXP-95837266')
except Shipment.DoesNotExist:
    pass

print('Done!')

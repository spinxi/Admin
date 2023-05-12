from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user
from django.db.models import Q
#FOR LOADS
STATUS_OPEN = 'OPEN'
STATUS_IN_TRANSIT = 'IN_TRANSIT'
STATUS_DELIVERED = 'DELIVERED'
STATUS_LOADS = (
    (STATUS_OPEN, 'Open'),
    (STATUS_IN_TRANSIT, 'In transit'),
    (STATUS_DELIVERED, 'Delivered')
)

class LoadManager(models.Manager):
    def get_loads(self, user=None, bill_to=None, starting_address=None, truck=None, include_all=False):
        queryset = self.all() if include_all else self.filter(load_status=STATUS_OPEN)
        if user is None and not include_all:
            user = get_user()  # Get the current user
        if user:
            queryset = queryset.filter(created_by=user)
        if bill_to:
            queryset = queryset.filter(bill_to=bill_to)
        if starting_address:
            queryset = queryset.filter(starting_address=starting_address)
        if truck:
            queryset = queryset.filter(truck=truck)
        return queryset

    def get_open_loads(self, user=None, bill_to=None):
        queryset = self.filter(load_status=STATUS_OPEN)
        if user is None:
            user = get_user()  # Get the current user
        queryset = queryset.filter(created_by=user)
        if bill_to:
            queryset = queryset.filter(bill_to=bill_to)
        return queryset

    def get_in_transit_loads(self, user=None, starting_address=None):
        queryset = self.filter(load_status=STATUS_IN_TRANSIT)
        if user is None:
            user = get_user()  # Get the current user
        queryset = queryset.filter(created_by=user)
        if starting_address:
            queryset = queryset.filter(starting_address=starting_address)
        return queryset

    def get_delivered_loads(self, user=None, truck=None):
        queryset = self.filter(load_status=STATUS_DELIVERED)
        if user is None:
            user = get_user()  # Get the current user
        queryset = queryset.filter(created_by=user)
        if truck:
            queryset = queryset.filter(truck=truck)
        return queryset
    def get_loads_by_group(self, group):
        return self.filter(Q(created_by__groups=group) | Q(updated_by__groups=group))


class Loads(models.Model):
    #Load information
    bill_to = models.CharField(max_length=50, default=None, null=True, blank=True)
    rate = models.DecimalField(default=None, null=True, blank=True, max_digits=6, decimal_places=2)
    truck = models.CharField(max_length=50, default=None)
    trailer = models.CharField(max_length=50, default=None)
    po_number = models.CharField(max_length=50, default=None, unique=True)
    load_status = models.CharField(choices=STATUS_LOADS, max_length=50, default=STATUS_OPEN)
    notes = models.TextField(max_length=200, default=None)
    starting_address = models.CharField(max_length=100, default=None, null=True, blank=True)
    coordinates_starting = models.JSONField(blank=True, null=True)
    #Hidden
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='create_load')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='update_load')

    objects = LoadManager()

    def get_delivery_location(self):
        if self.loaddelivery.exists():
            return self.loaddelivery.first().delivery_location
        return None

    def get_pickup_location(self):
        if self.loadpickup.exists():
            return self.loadpickup.first().pickup_location
        return None

    def get_driver_names(self):
        return ', '.join([driver.username for driver in self.loaddrivers.all()])

    def is_late(self):
        
        if not self.loaddelivery.exists():
            return False, None

        delivery_date = self.loaddelivery.first().delivery_date_to

        if delivery_date is None:
            return False, None

        # Adjust delivery date to UTC time zone
        delivery_date = delivery_date.astimezone(timezone.utc)

        is_late = delivery_date < timezone.now()
        time_difference = timezone.now()

        return is_late, time_difference

class LoadDelivery(models.Model):
    load = models.ForeignKey(Loads, on_delete=models.DO_NOTHING, related_name="loaddelivery")
    delivery_location = models.CharField(max_length=100, default=None, null=True, blank=True)
    delivery_date_from = models.DateTimeField(default=None, blank=True, null=True)
    delivery_date_to = models.DateTimeField(default=None, blank=True, null=True)
    coordinates_delivery = models.JSONField(blank=True, null=True)

class LoadPickup(models.Model):
    load = models.ForeignKey(Loads, on_delete=models.DO_NOTHING, related_name="loadpickup")
    pickup_location = models.CharField(max_length=100, default=None, null=True, blank=True)
    pickup_date_from = models.DateTimeField(default=None, blank=True, null=True)
    pickup_date_to = models.DateTimeField(default=None, blank=True, null=True)
    coordinates_pickup = models.JSONField(blank=True, null=True)
     

class LoadCharges(models.Model):
    load = models.ForeignKey(Loads, on_delete=models.DO_NOTHING, related_name="loadcharges")
    charges = models.CharField(choices=STATUS_LOADS, max_length=50, default=STATUS_OPEN)
    charges_rate = models.DecimalField(default=None, null=True, blank=True, max_digits=6, decimal_places=2)
          
class LoadFiles(models.Model):
    files = models.FileField(upload_to="Loads/%Y-%m-%d/", blank=True, null=True)
    key = models.ForeignKey('Loads', on_delete=models.DO_NOTHING, related_name="loadfiles")

class LoadDrivers(models.Model):
    load_driver_user = models.ManyToManyField(CustomUser)
    load_key = models.ForeignKey(Loads, on_delete=models.DO_NOTHING, related_name="loaddrivers")


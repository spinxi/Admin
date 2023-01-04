from django.db import models
from users.models import CustomUser
from trailer.models import Trailer

STATUS = (('Open', 'Open'), ('Covered', 'Covered'), ('Dispatched', 'Dispatched'), ('Loading', 'Loading'), ('On route', 'On route'), ('Unloading', 'Unloading'), ('In yard', 'In yard'))
class Loads(models.Model):
    #Load information
    bill_to = models.CharField(max_length=50, default=None, null=True, blank=True)
    # models.ModelChoiceField(queryset=CustomUser.objects.filter(is_driver=True), empty_label=None)
    rate = models.IntegerField(default=None, null=True, blank=True)
    # type = models.CharField(max_length=50, default=None)
    # rate = models.IntegerField(default=None)
    driver = models.CharField(choices=STATUS ,max_length=50, default=None)
    truck = models.CharField(max_length=50, default=None)
    trailer = models.CharField(max_length=50, default=None)
    po_number = models.CharField(max_length=50, default=None, unique=True)
    load_status = models.CharField(choices=STATUS, max_length=50, default="Open")
    notes = models.TextField(max_length=200, default=None)
    #Pick
    pickup_location = models.CharField(max_length=100, default=None, null=True, blank=True)
    pickup_date = models.DateField(default=None, blank=True, null=True)
    pickup_time = models.TimeField(default=None, blank=True, null=True)
    #Delivery
    delivery_location = models.CharField(max_length=100, default=None, null=True, blank=True)
    delivery_date = models.DateField(default=None, blank=True, null=True)
    delivery_time = models.TimeField(default=None, blank=True, null=True)
    #Hidden
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='create_load')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='update_load')

class LoadFiles(models.Model):
    files = models.FileField(upload_to="Loads/%Y-%m-%d/", blank=True, null=True)
    key = models.ForeignKey('Loads', on_delete=models.CASCADE)

class LoadDrivers(models.Model):
    load = models.ForeignKey(Loads, on_delete=models.DO_NOTHING)
    load_drivers = models.CharField(max_length=50, default=None)
    load_driver_type = models.CharField(max_length=50, default=None)
    
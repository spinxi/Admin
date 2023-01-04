from django.db import models
import pghistory, pgtrigger
from users.models import CustomUser

RENT = ((0, 'No'), (1, 'Yes'))
STATUS = ((0, 'active'), (1, 'Need Check'), (2, 'Inactive'))
TRAILER_STATUS =  (('Owner-Operator', 'Owner-Operator'), ('GA', 'GA'), ('Self Dot', 'Self Dot'))
GPS =  (('Azuga', 'Azuga'), ('Verizon', 'Verizon'))

@pghistory.track(pghistory.Snapshot(), fields=["plate_number"], model_name="TrailerTracker")
class Trailer(models.Model):
    #Trailer
    trailer_status = models.CharField(choices=TRAILER_STATUS, max_length=50, default='Owner-Operator', null=True, blank=True)
    unit_number = models.CharField(max_length=50, default=None, null=True, blank=True)
    vin_number = models.CharField(default=None, max_length=50, null=True, blank=True)
    plate_number = models.CharField(default=None, max_length=50, null=True, blank=True)
    year = models.IntegerField(default=None, null=True, blank=True )
    state = models.CharField(max_length=50, default=None, null=True, blank=True)
    make = models.CharField(max_length=50, default=None, null=True, blank=True)
    registration_start_date = models.DateField(default=None)
    registration_expiration_date = models.DateField(default=None)
    inspection_expiration_date = models.DateField(default=None)
    #Insurance
    physical_damage_expiration_date = models.DateField(default=None)
    non_trucking_expiration_date = models.DateField(default=None)
    cargo_expiration_date = models.DateField(default=None)
    #Safety
    gps = models.CharField(choices=GPS, max_length=50, default='Azuga', null=True, blank=True)
    gps_serial_number = models.CharField(max_length=50, default=None, null=True, blank=True)
    #Status
    rent = models.BooleanField(choices=RENT, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    #Exclude-
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='create_trailer')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='update_trailer')
class TrailerFiles(models.Model):
    files = models.FileField(upload_to="trailers/%Y-%m-%d/", blank=True, null=True)
    trailer_files = models.ForeignKey('Trailer', on_delete=models.CASCADE, default=None, null=True)
    date_created_trailer_files = models.DateTimeField(auto_now_add=True)





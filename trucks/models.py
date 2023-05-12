from django.db import models
import pghistory, pgtrigger
from users.models import CustomUser


STATUS = ((0, 'active'), (1, 'Need Check'), (2, 'Inactive'))
TRAILER_STATUS =  (('Owner-Operator', 'Owner-Operator'), ('GA', 'GA'), ('Self Dot', 'Self Dot'))
GPS =  (('Azuga', 'Azuga'), ('Verizon', 'Verizon'))
CAMERA =  (('Azuga', 'Azuga'), ('Verizon', 'Verizon'))
TABLET_OWNER =  (('GA Logistics', 'GA Logistics'), ('Driver', 'Driver'))
FUEL_CARD = (('GA Logistics', 'GA Logistics'), ('Driver', 'Driver'))
EZ_PASS = (('GA Logistics', 'GA Logistics'), ('Driver', 'Driver'))
@pghistory.track(pghistory.Snapshot(),
    fields=["plate_number", "owner", "registrant"], model_name="TruckTracker")
class Trucks(models.Model):
    #Truck
    truck_status = models.CharField(choices=TRAILER_STATUS, max_length=50, default='Owner-Operator')
    unit_number = models.CharField(max_length=50, default=None, null=True, blank=True)
    vin_number = models.CharField(default=None, max_length=50, null=True, blank=True)
    plate_number = models.CharField(default=None, max_length=50, null=True, blank=True) #Need History
    year = models.IntegerField(default=None, null=True, blank=True )
    state = models.CharField(max_length=50, default=None, null=True, blank=True)
    make = models.CharField(max_length=50, default=None, null=True, blank=True)
        #driver is owner
    owner = models.CharField(max_length=50, default=None, null=True, blank=True) #Need History
        #END driver is owner
    registrant = models.CharField(max_length=50, default=None, null=True, blank=True) #Need History

    registration_start_date = models.DateField(default=None, null=True, blank=True)
    registration_expiration_date = models.DateField(default=None, null=True, blank=True)
    inspection_expiration_date = models.DateField(default=None, null=True, blank=True)

        #if state inspection is on
    state_inspection = models.BooleanField(default=False) #Need History
    state_inspection_expiration_date = models.DateField(default=None, null=True, blank=True) #Need History
    state_inspection_title_owner = models.CharField(max_length=50, default=None, null=True, blank=True)
    state_inspection_hut_num = models.CharField(max_length=50, default=None, null=True, blank=True)
    state_inspection_ifta_num = models.CharField(max_length=50, default=None, null=True, blank=True)
        #END if state inspection is on

    #Insurance
    physical_damage_expiration_date = models.DateField(default=None, null=True, blank=True)
    non_trucking_expiration_date = models.DateField(default=None, null=True, blank=True)
    cargo_expiration_date = models.DateField(default=None, null=True, blank=True)
    #Safety
    gps = models.CharField(choices=GPS, max_length=50, default='Azuga')
    gps_serial_number = models.CharField(max_length=50, default=None, null=True, blank=True)
    camera = models.CharField(choices=CAMERA, max_length=50, default='Azuga')
    camera_serial_number = models.CharField(max_length=50, default=None, null=True, blank=True)
    #Tablet
    tablet_imei = models.CharField(max_length=50, default=None, null=True, blank=True)
    tablet_owner = models.CharField(choices=TABLET_OWNER,max_length=50, default='GA Logistics')
    #Fuel
    fuel_card = models.CharField(choices=FUEL_CARD, default="Ga Logistics", max_length=50)
    who_is_driver = models.CharField(max_length=50, default=None, null=True, blank=True)
    fuel_card_type = models.CharField(max_length=50, default=None, null=True, blank=True)
    card_start_date = models.CharField(max_length=50, default=None, null=True, blank=True)
    #EZ Pass
    ez_pass = models.CharField(choices=EZ_PASS, default="Ga Logistics", max_length=50)
    who_is_driver_ezpass = models.CharField(max_length=50, default=None, null=True, blank=True)
    ez_pass_num = models.CharField(max_length=50, default=None, null=True, blank=True)
        #EZ Pass if it's OUR
    ez_pass_start_date = models.CharField(max_length=50, default=None, null=True, blank=True)
    #Status
    rent = models.BooleanField(default=False)
    #Exclude-
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='create_truck')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='update_truck')
class TruckFiles(models.Model):
    files = models.FileField(upload_to="trucks/%Y-%m-%d/", blank=True, null=True)
    truck_files = models.ForeignKey('Trucks', on_delete=models.CASCADE, default=None, null=True)
    date_created_truck_files = models.DateTimeField(auto_now_add=True)

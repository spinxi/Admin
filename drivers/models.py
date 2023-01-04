from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from datetime import datetime
STATUS = ((0, 'Inactive'), (1, 'Active'))
US_STATES = (
    ("AL", 'Alabama'), 
    ("AK", 'Alaska'),
    ("AZ", 'Arizona'), 
    ("AR", 'Arkansas'),
    ("CA", 'California'), 
    ("CO", 'Colorado'),
    ("CT", 'Connecticut'), 
    ("DE", 'Delaware'),
    ("DC", 'District Of Columbia'), 
    ("FL", 'Florida'),
    ("GA", 'Georgia'), 
    ("HI", 'Hawaii'),
    ("ID", 'Idaho'), 
    ("IL", 'Illinois'),
    ("IN", 'Indiana'), 
    ("IA", 'Iowa'),
    ("KS", 'Kansas'), 
    ("KY", 'Kentucky'),
    ("LA", 'Louisiana'), 
    ("ME", 'Maine'),
    ("MD", 'Maryland'), 
    ("MA", 'Massachusetts'),
    ("MI", 'Michigan'), 
    ("MN", 'Minnesota'),
    ("MS", 'Mississippi'), 
    ("MO", 'Missouri'),
    ("MT", 'Montana'), 
    ("NE", 'Nebraska'),
    ("NV", 'Nevada'), 
    ("NH", 'New Hampshire'),
    ("NJ", 'New Jersey'), 
    ("NM", 'New Mexico'),
    ("NY", 'New York'), 
    ("NC", 'North Carolina'),
    ("ND", 'North Dakota'), 
    ("OH", 'Ohio'),
    ("OK", 'Oklahoma'), 
    ("OR", 'Oregon'),
    ("PA", 'Pennsylvania'), 
    ("RI", 'Rhode Island'),
    ("SC", 'South Carolina'), 
    ("SD", 'South Dakota'),
    ("TN", 'Tennessee'), 
    ("TX", 'Texas'),
    ("UT", 'Utah'), 
    ("VT", 'Vermont'),
    ("VA", 'Virginia'), 
    ("WA", 'Washington'),
    ("WV", 'West Virginia'), 
    ("WI", 'Wisconsin'),
    ("WY", 'Wyoming')
    )

class Driver(models.Model):
    #Driver's info
    driver_user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    full_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    birth_date = models.DateField(default=None, blank=True, null=True)
    address = models.CharField(max_length=70, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    driver_status = models.IntegerField(choices=STATUS, default=1)
        #age
        #license upload
    license_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_state = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_class = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_exp_date = models.DateField(default=None, blank=True, null=True)

    #Drug Test - Need all history
        #file upload
    last_drug_test = models.DateField(default=None, blank=True, null=True)
    drug_test_status = models.CharField(max_length=50, default=None, blank=True, null=True)
    drug_test_result = models.BooleanField(default=False, blank=True, null=True)
    #OCC
    member_number = models.CharField(max_length=50, default=None, blank=True, null=True)
        #upload
    occ_start_date = models.DateField(default=None, blank=True, null=True)
    occ_exp_date = models.DateField(default=None, blank=True, null=True)

    #Medical Certificate
    med_cert_exp_date = models.DateField(default=None, blank=True, null=True)
    med_cert = models.BooleanField(default=False, blank=True, null=True)
    #PSP
    med_cert = models.BooleanField(default=False, blank=True, null=True)
    #MVR
    mvr_status = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_mvr = models.DateField(default=None, blank=True, null=True)

    #Contract
    contract_sign_date = models.DateField(default=None, blank=True, null=True)

    #pev
    pev_first_send = models.DateField(default=None, blank=True, null=True)
    pev_second_send = models.DateField(default=None, blank=True, null=True)
    pev_receive_date = models.DateField(default=None, blank=True, null=True)

    #W9
    w9 = models.BooleanField(default=False, blank=True, null=True)
    w9_company_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    w9_company_ein = models.CharField(max_length=50, default=None, blank=True, null=True)
    w9_company_address = models.CharField(max_length=50, default=None, blank=True, null=True)
    #Beneficiary info
    ben_full_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    ben_address = models.CharField(max_length=50, default=None, blank=True, null=True)
    ben_relation = models.CharField(max_length=50, default=None, blank=True, null=True)
    #Safety Deposit
    safety_received_date = models.DateField(default=None, blank=True, null=True)
    safety_received_amount = models.CharField(max_length=50, default=None, blank=True, null=True)
    safety_return_date = models.DateField(default=None, blank=True, null=True)
    safety_returned_amount = models.CharField(max_length=50, default=None, blank=True, null=True)
    safety_charge_date = models.DateField(default=None, blank=True, null=True)
    safety_charge_amount = models.CharField(max_length=50, default=None, blank=True, null=True)
    safety_charge_reason = models.CharField(max_length=50, default=None, blank=True, null=True)

    next_drug_test = models.DateField(default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    def get_age(self):
        age = datetime.date.today()-self.birth_date
        return int((age).days/365.25)
    def __str__(self):
	    return self.full_name
        
class DriversFiles(models.Model):
    file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    driver_files = models.ForeignKey('Driver', on_delete=models.CASCADE, default=None, null=True)

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.is_driver:
            Driver.objects.create(
                driver_user=instance, 
                full_name = None,
                phone_number = None,
                address = None,
                country = None,
                state = None,
                city = None,
                zipp = None,
                birth_date = None,
                license_no = None,
                license_exp_date = None,
                last_medical= None,
                next_medical = None,
                last_drug_test = None,
                next_drug_test = None,
                )
        # if instance.user_type == 2:
        #     Staffs.objects.create(admin=instance)
        # if instance.user_type == 3:
        #     Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    

@receiver(post_save, sender=Driver)
def save_user_profile(sender, instance, **kwargs):
    if instance.driver_user:
        instance.driver_user.save()
    # if instance.user_type == 2:
    #     instance.staffs.save()
    # if instance.user_type == 3:
    #     instance.students.save()
@receiver(post_delete, sender=Driver)
def delete_user_profile(sender, instance, **kwargs):
    print(instance.driver_user)
    if instance.driver_user: # just in case user is not specified
        instance.driver_user.delete()

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from django.contrib.postgres.fields import JSONField
STATUS = ((0, "Inactive"), (1, "Active"))
DRUG_TEST_STATUS = (
    ("Pre-employement", "Pre-employement"), 
    ("Random", "Random"),
    ("Post-Accident drug", "Post-Accident drug"),
    ("Post-accident Alcohol", "Post-accident Alcohol"),
    ("Follow up", "Follow up")
    )
MVR_STATUS= (
    ("Pre-employement", "Pre-employement"),
    ("Medical Renewal", "Medical Renewal"),
    ("License Renewal", "License Renewal"),
    ("After 1 Year", "After 1 Year")
    )
DRUG_TEST_RESULT= (
    (True, "Positive"), 
    (False, "Negative")
    )
MED_VERIFICATION= (
    (True, "Yes"), 
    (False, "No")
    )
FED_CLASSICIFATION= (
    ("Individual/Sole proprietor or single-member LLC", "Individual/Sole proprietor or single-member LLC"),
    ("C Corporation", "C Corporation"),
    ("S Corporation", "S Corporation"),
    ("Partnership", "Partnership"),
    ("Trust/Estate single-member LLC", "Trust/Estate single-member LLC"),
    ("Limited libility company", "Limited libility company"),
    ("Other", "Other"),
    )
US_STATES = (
    ("AL", "Alabama"), 
    ("AK", "Alaska"),
    ("AZ", "Arizona"), 
    ("AR", "Arkansas"),
    ("CA", "California"), 
    ("CO", "Colorado"),
    ("CT", "Connecticut"), 
    ("DE", "Delaware"),
    ("DC", "District Of Columbia"), 
    ("FL", "Florida"),
    ("GA", "Georgia"), 
    ("HI", "Hawaii"),
    ("ID", "Idaho"), 
    ("IL", "Illinois"),
    ("IN", "Indiana"), 
    ("IA", "Iowa"),
    ("KS", "Kansas"), 
    ("KY", "Kentucky"),
    ("LA", "Louisiana"), 
    ("ME", "Maine"),
    ("MD", "Maryland"), 
    ("MA", "Massachusetts"),
    ("MI", "Michigan"), 
    ("MN", "Minnesota"),
    ("MS", "Mississippi"), 
    ("MO", "Missouri"),
    ("MT", "Montana"), 
    ("NE", "Nebraska"),
    ("NV", "Nevada"), 
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"), 
    ("NM", "New Mexico"),
    ("NY", "New York"), 
    ("NC", "North Carolina"),
    ("ND", "North Dakota"), 
    ("OH", "Ohio"),
    ("OK", "Oklahoma"), 
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"), 
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"), 
    ("SD", "South Dakota"),
    ("TN", "Tennessee"), 
    ("TX", "Texas"),
    ("UT", "Utah"), 
    ("VT", "Vermont"),
    ("VA", "Virginia"), 
    ("WA", "Washington"),
    ("WV", "West Virginia"), 
    ("WI", "Wisconsin"),
    ("WY", "Wyoming")
    )

class Driver(models.Model):
    driver_user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    #Basic Info -- 1

    full_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    birth_date = models.DateField(default=None, blank=True, null=True)
    current_address = models.CharField(max_length=70, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    driver_status = models.IntegerField(choices=STATUS, default=1)

    #License
    license_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_address = models.CharField(max_length=70, default=None, blank=True, null=True)
    license_state = models.CharField(choices=US_STATES,max_length=50, default=None, blank=True, null=True)
    license_class = models.CharField(max_length=50, default=None, blank=True, null=True)
    license_issue = models.DateField(default=None, blank=True, null=True)
    license_exp_date = models.DateField(default=None, blank=True, null=True)

    # #Drug Test - Need all history
    last_drug_test = models.DateField(default=None, blank=True, null=True)
    drug_test_status = models.CharField(choices=DRUG_TEST_STATUS,max_length=40, default=None, blank=True, null=True)
    drug_test_result = models.BooleanField(choices=DRUG_TEST_RESULT, default=False, blank=True, null=True)

    # #OCC

    occ_member_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    occ_start_date = models.DateField(default=None, blank=True, null=True)
    occ_cancel_date = models.DateField(default=None, blank=True, null=True)

    # #Medical Certificate

    med_cert_exp_date = models.DateField(default=None, blank=True, null=True)
    med_verification = models.BooleanField(choices=MED_VERIFICATION, default=False, blank=True, null=True)

    #Clearing House Date -- 1
    clearing_house_date = models.DateField(default=None, blank=True, null=True)


    #PSP -- 1
    psp = models.BooleanField(choices=MED_VERIFICATION, default=False, blank=True, null=True)

    #MVR -- 1

    mvr_status = models.CharField(choices=MVR_STATUS, max_length=50, default=None, blank=True, null=True)
    last_mvr = models.DateField(default=None, blank=True, null=True)

    #Contract -- 1

    contract_sign_date = models.DateField(default=None, blank=True, null=True)

    #PEV

    pev_first_send = models.DateField(default=None, blank=True, null=True)
    pev_second_send = models.DateField(default=None, blank=True, null=True)
    pev_receive_date = models.DateField(default=None, blank=True, null=True)

    #W9 (If Yes)

    w9 = models.BooleanField(default=False, blank=True, null=True)
    w9_company_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    w9_company_ein = models.CharField(max_length=50, default=None, blank=True, null=True)
    w9_company_address = models.CharField(max_length=50, default=None, blank=True, null=True)
    w9_federal_classificaton = models.CharField(choices=FED_CLASSICIFATION,max_length=50, default=None, blank=True, null=True)

    #Bank Information

    bank_holder_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_holder_address = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_city = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_state = models.CharField(choices=US_STATES, max_length=50, default=None, blank=True, null=True)
    bank_zip_code = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_routing_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_account_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_personal_checking = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_business_checking = models.CharField(max_length=50, default=None, blank=True, null=True)
    bank_personal_saving = models.CharField(max_length=50, default=None, blank=True, null=True)

    #Application
 
    application_fill_date = models.DateField(default=None, blank=True, null=True)

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

    ## exclude
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return self.full_name
        
class DriversFiles(models.Model):
    ben_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    application_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    bank_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    w9_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    pev_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    contract_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    mvr_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    medical_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    occ_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    license_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    drug_test_file = models.FileField(upload_to="drivers/%Y-%m-%d/", blank=True, null=True)
    driver_files = models.ForeignKey("Driver", on_delete=models.CASCADE, default=None, null=True)

# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will automatically insert data in HOD, Staff or Student
# def create_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted)
#     if created:
#         # Check the user_type and insert the data in respective tables
#         if instance.is_driver:
#             Driver.objects.create(
#                 driver_user=instance, 
#                 full_name = None,
#                 phone_number = None,
#                 # address = None,
#                 # country = None,
#                 # state = None,
#                 # city = None,
#                 # zipp = None,
#                 # birth_date = None,
#                 # license_no = None,
#                 # license_exp_date = None,
#                 # last_medical= None,
#                 # next_medical = None,
#                 # last_drug_test = None,
#                 # next_drug_test = None,
#                 )
            


        # if instance.user_type == 2:
        #     Staffs.objects.create(admin=instance)
        # if instance.user_type == 3:
        #     Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    

# @receiver(post_save, sender=Driver)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.driver_user:
#         instance.driver_user.save()
#     # if instance.user_type == 2:
#     #     instance.staffs.save()
#     # if instance.user_type == 3:
#     #     instance.students.save()
# @receiver(post_delete, sender=Driver)
# def delete_user_profile(sender, instance, **kwargs):
#     print(instance.driver_user)
#     if instance.driver_user: # just in case user is not specified
#         instance.driver_user.delete()

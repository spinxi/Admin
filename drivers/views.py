from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import CustomUser
from drivers.models import Driver, DriversFiles
from users.forms import CustomUserForm
from drivers.forms import DriverForm, DriverFormUpload
from users.decorators import driver_access_only
from drivers.helpers import handle_files
from django.shortcuts import get_object_or_404



#Create Drivers
@login_required(redirect_field_name=None)
# @driver_access_only()
def create_driver_view(request):
    if request.method == "POST":
        add_driver = DriverForm(request.POST)
        add_custom_user = CustomUserForm(request.POST)
        add_driver_files = DriverFormUpload(request.FILES)
        if add_custom_user.is_valid() and add_driver.is_valid() :
            try:
                #For Custom User
                instance = add_custom_user.save(commit=False)
                instance.is_driver = True
                instance.set_password("password1234")
                instance.save()

                driver = add_driver.save(commit=False)
                driver.driver_user = instance
                driver.save()
                file_dict = {
                    'ben_file': request.FILES.getlist('ben_file'),
                    'application_file': request.FILES.getlist('application_file'),
                    'bank_file': request.FILES.getlist('bank_file'),
                    'w9_file': request.FILES.getlist('w9_file'),
                    'pev_file': request.FILES.getlist('pev_file'),
                    'contract_file': request.FILES.getlist('contract_file'),
                    'mvr_file': request.FILES.getlist('mvr_file'),
                    'medical_file': request.FILES.getlist('medical_file'),
                    'occ_file': request.FILES.getlist('occ_file'),
                    'license_file': request.FILES.getlist('license_file'),
                    'drug_test_file': request.FILES.getlist('drug_test_file'),
                }
                handle_files(file_dict, driver)

                messages.success(request, "Driver Has Been Added Successfully!")

                return redirect('drivers:drivers.all')
            except:
                messages.error(request, "Failed To Add Driver!")
                return redirect('drivers:drivers.add')
        else:
            print(add_driver.errors)
            
    else:
        add_driver = DriverForm()
        add_driver_files = DriverFormUpload()
        add_custom_user = CustomUserForm()
    return render(request, "drivers/drivers-add.html", {"add_driver": add_driver, "add_driver_files": add_driver_files, "add_custom_user": add_custom_user})


#Show all Drivers
@login_required(redirect_field_name=None)
def list_driver_view(request):
    driver_list = Driver.objects.all().order_by('-date_created')
    context = {
        'driver_list': driver_list,
    }
    return render(request, 'drivers/drivers-all.html', context)

   

#Show Driver's Profile
@login_required(redirect_field_name=None)
def profile_driver_view(request, id):
    driver = Driver.objects.get(driver_user_id=id)
    context = {
        'driver': driver,
    }
    return render(request, 'drivers/drivers-profile.html', context)


#Edit Drivers
def edit_driver_view(request, driver_id):
    driver = get_object_or_404(Driver, driver_user=driver_id)

    if request.method == "POST":
        add_driver = DriverForm(request.POST, instance=driver)
        add_custom_user = CustomUserForm(request.POST, instance=driver.driver_user)
        add_driver_files = DriverFormUpload(request.FILES)

        if add_custom_user.is_valid() and add_driver.is_valid() :
            try:
                # Save the updated driver and custom user objects
                add_custom_user.save()
                driver = add_driver.save()

                # Delete the old files related to the driver object
                # delete_driver_files(driver)

                # Save the new files related to the driver object
                file_dict = {
                    'ben_file': request.FILES.getlist('ben_file'),
                    'application_file': request.FILES.getlist('application_file'),
                    'bank_file': request.FILES.getlist('bank_file'),
                    'w9_file': request.FILES.getlist('w9_file'),
                    'pev_file': request.FILES.getlist('pev_file'),
                    'contract_file': request.FILES.getlist('contract_file'),
                    'mvr_file': request.FILES.getlist('mvr_file'),
                    'medical_file': request.FILES.getlist('medical_file'),
                    'occ_file': request.FILES.getlist('occ_file'),
                    'license_file': request.FILES.getlist('license_file'),
                    'drug_test_file': request.FILES.getlist('drug_test_file'),
                }
                handle_files(file_dict, driver)

                messages.success(request, "Driver Has Been Updated Successfully!")

                return redirect('drivers:drivers.all')
            except:
                messages.error(request, "Failed To Update Driver!")
                return redirect('drivers:drivers.edit', driver_id=driver_id)
        else:
            print(add_driver.errors)
            
    else:
        add_driver = DriverForm(instance=driver)
        add_driver_files = DriverFormUpload()
        add_custom_user = CustomUserForm(instance=driver.driver_user)
    
    return render(request, "drivers/drivers-add.html", {"add_driver": add_driver, "add_driver_files": add_driver_files, "add_custom_user": add_custom_user})


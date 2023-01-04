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
from django.urls import reverse_lazy

@login_required(redirect_field_name=None)
# @driver_access_only()
#Create Drivers
def create_driver_view(request):
    if request.method == "POST":
        #Get Forms
        add_driver = DriverForm(request.POST)
        add_user_email = CustomUserForm(request.POST)
        add_driver_files = DriverFormUpload(request.FILES)
        add_driver_file = request.FILES.getlist("file")
        for i in add_driver_files:
            print(i)
        #Check Validation
        if add_driver.is_valid() and add_user_email.is_valid():
            #For Custom User
            password = 'Ga20224$5%'
            full_name = add_driver.cleaned_data['full_name']
            email = add_user_email.cleaned_data['email']
            phone_number = add_driver.cleaned_data['phone_number']
            address = add_driver.cleaned_data['address']
            country = add_driver.cleaned_data['country']
            state = add_driver.cleaned_data['state']
            city = add_driver.cleaned_data['city']
            zipp = add_driver.cleaned_data['zipp']
            birth_date = add_driver.cleaned_data['birth_date']
            license_no = add_driver.cleaned_data['license_no']
            
            license_exp_date = add_driver.cleaned_data['license_exp_date']
            last_medical = add_driver.cleaned_data['last_medical']
            next_medical = add_driver.cleaned_data['next_medical']
            last_drug_test = add_driver.cleaned_data['last_drug_test']
            next_drug_test = add_driver.cleaned_data['next_drug_test']
            try:
                user = CustomUser.objects.create_user(
                    password = password, 
                    is_driver = True, 
                    email = email
                    )
                #For Driver Profile
                user.driver.full_name = full_name
                user.driver.phone_number=phone_number
                user.driver.address = address
                user.driver.country = country
                user.driver.state = state
                user.driver.city = city
                user.driver.zipp = zipp
                user.driver.birth_date = birth_date
                user.driver.license_no = license_no
                user.driver.license_exp_date = license_exp_date
                user.driver.last_medical = last_medical
                user.driver.next_medical = next_medical
                user.driver.last_drug_test = last_drug_test
                user.driver.next_drug_test = next_drug_test
                user.save()
                for i in add_driver_file:
                    DriversFiles.objects.create(driver_files=user.driver, file=i)
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
        add_user_email = CustomUserForm()
    return render(request, "drivers/drivers-add.html", {"add_driver": add_driver, "add_driver_files": add_driver_files, "add_user_email": add_user_email})

#Show all Drivers
@login_required(redirect_field_name=None)
def list_driver_view(request):
    driver_list = Driver.objects.all().order_by('-date_created')
    users = CustomUser.objects.all()
    countyData = (users)
    context = {
        'driver_list': driver_list,
        'users': users,
        'countyData': countyData,
    }
    return render(request, 'drivers/drivers-all.html', context)

#Show Driver's Profile
def profile_driver_view(request, id):
    user = CustomUser.objects.get(id=id)
    driver = Driver.objects.get(driver_user_id=id)
    # Handling non authenticated user for obvious reasons
    # if request.user.is_authenticated() and request.user == user:
    #     editable = True

    context = {
        'user': user,
        'driver': driver,
    }
    return render(request, 'drivers/drivers-profile.html', context)

#Edit Drivers
def edit_driver_view(request, id):
    add_driver_files = DriverFormUpload(request.FILES)
    driver = CustomUser.objects.get(id=id)
    driver2 = Driver.objects.get(driver_user_id=id)
    add_driver = DriverForm(request.POST or None, instance = driver2)
    add_user_email = CustomUserForm(request.POST or None, instance = driver)
    add_driver_file = request.FILES.getlist("file")
    if add_driver.is_valid():
        add_driver.save()
        add_user_email.save()
        for i in add_driver_file:
            DriversFiles.objects.create(driver_files=driver2, file=i)
        messages.success(request, "Driver Has Been Added Successfully!")
        return redirect('drivers:drivers.all')
    return render(request, 'drivers/drivers-add.html', {'add_driver' : add_driver, 'add_user_email':add_user_email, 'add_driver_files' : add_driver_files, 'driver' : driver})

#Delete Drivers
def delete_driver_view(request, id):
    driver = Driver.objects.get(driver_user=id)
    # try:
    driver.delete()
    messages.success(request, "Driver Has Been Deleted Successfully!")
    return HttpResponseRedirect(reverse('drivers:drivers.all'))
    # except:
    #     messages.error(request, "Failed To Delete Driver!")
    #     return HttpResponseRedirect(reverse('drivers:drivers.all'))
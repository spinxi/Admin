from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Trucks, TruckFiles
from .forms import TrucksForm, TruckFormUpload
from users.decorators import driver_access_only

import uuid
from django.urls import reverse_lazy

# @login_required
# @driver_access_only()
#Create Drivers
def create_truck_view(request):
    if request.method == "POST":
        truck_form = TrucksForm(request.POST)
        add_truck_files = TruckFormUpload(request.FILES)
        add_truck_file = request.FILES.getlist("file")
        if truck_form.is_valid():
            f = truck_form.save(commit=False)
            f.user = request.user
            f.save()
            for i in add_truck_file:
                TruckFiles.objects.create(truck_files=f, file=i)
            messages.success(request, "Truck Has Been Added Successfully!")
            return redirect('trucks:trucks.all')
        else:
            print(truck_form.errors)
    else:
        truck_form = TrucksForm()
        add_truck_files = TruckFormUpload()

    return render(request, "trucks/trucks-add.html", {"truck_form": truck_form, "add_truck_files": add_truck_files})

#Show all Drivers
def list_truck_view(request):
    truck_list = Trucks.objects.all()
    context = {
        'truck_list': truck_list,
    }
    return render(request, 'trucks/trucks-all.html', context)
#Edit Drivers
def edit_truck_view(request, id):
    trucks = Trucks.objects.get(id=id)
    truck_form = TrucksForm(request.POST or None, instance = trucks)
    add_truck_files = TruckFormUpload(request.FILES)

    add_truck_file = request.FILES.getlist("file")
    if truck_form.is_valid():
        f = truck_form.save(commit=False)
        f.created_by = trucks.created_by
        f.updated_by = request.user
        f.save()
        for i in add_truck_file:
            TruckFiles.objects.create(truck_files=f, files=i)
        messages.success(request, "Truck Has Been Edited Successfully!")
        return redirect('trucks:trucks.all')
    return render(request, 'trucks/trucks-add.html', {'add_truck_files' : add_truck_files, 'truck_form':truck_form})

<<<<<<< HEAD
# from django.shortcuts import render, redirect
# from loads.models import Loads, LoadFiles, LoadDrivers
# from loads.forms import LoadForm, LoadFormUpload, LoadDriversForm, BookFormSet
# from django.contrib import messages
# # Create your views here.

# def create_load_view(request):
#     if request.method == "POST":
#         load_form = LoadForm(request.POST)
#         load_drivers = LoadDriversForm(request.POST)
#         load_file_form = LoadFormUpload(request.FILES)
#         load_files = request.FILES.getlist("files")
#         # GET ALL DRIVERS
#         formset = BookFormSet(request.POST)
#         if (load_form.is_valid() ):
#             #FORMSET and formset.is_valid()
#             f = load_form.save(commit=False)
#             f.created_by = request.user
#             f.save()
#             # load_many_drivers = load_drivers.save(commit=False)
#             # load_many_drivers.load22 = f
#             # load_many_drivers.save()
#             # formset.load = f
#             # for form in formset:
#             #     # so that `question` instance can be attached.
#             #     print(form.cleaned_data)
#             #     driver = form.save(commit=False)
#             #     driver.load = f
#             #     driver.save()
#             for i in load_files:
#                 LoadFiles.objects.create(key=f, files=i)
#                 # load_file_form.save()
#             messages.success(request, "Load Has Been Added Successfully!")
#             return redirect('loads:load.all')
#         else:
#             messages.error(request, "Required Fields May Not Be Filled")
#             print(load_drivers.errors)
#     else:
#         formset = BookFormSet(queryset = Loads.objects.none())
#         load_form = LoadForm()
#         load_drivers = LoadDriversForm()
#         load_file_form = LoadFormUpload()
#     return render(request, "loads/loads-add.html", { "load_drivers":load_drivers, "load_form": load_form, "load_file_form": load_file_form})
# # apex dazgveva , load, misamartebi, 
# #Show all Drivers
# def list_load_view(request):
#     load_list = Loads.objects.order_by('-date_created')
#     context = {
#         'load_list': load_list,
#     }
#     return render(request, 'loads/loads-all.html', context)
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Loads, LoadFiles, LoadDrivers, LoadDelivery,LoadPickup
from .forms import LoadForm, LoadFilesForm, LoadDriversForm, LoadDeliveryFormset, LoadPickupFormset
from django.core.paginator import Paginator


@login_required
def create_load(request):
    if request.method == 'POST':
        load_form = LoadForm(request.POST)
        load_drivers_form = LoadDriversForm(request.POST)
        load_files_form = LoadFilesForm(request.POST, request.FILES)
        load_pickup_form = LoadPickupFormset(request.POST, instance=None, prefix='load_pickup_formset')
        load_delivery_form = LoadDeliveryFormset( request.POST, instance=None, prefix='load_delivery_formset')

        if (load_drivers_form.is_valid() and load_form.is_valid() and load_files_form.is_valid()):
            load = load_form.save(commit=False)
            load.created_by = request.user
            # load.updated_by = request.user
            load.save()

            load_drivers = load_drivers_form.save(commit=False)
            load_drivers.load_key = load
            load_drivers.save()
            load_drivers_form.save_m2m()

            load_pickup_form = LoadPickupFormset(request.POST, instance=load, prefix='load_pickup_formset')
            if load_pickup_form.is_valid():
                load_pickup_form.save()
                
            load_delivery_form = LoadDeliveryFormset(request.POST, instance=load, prefix='load_delivery_formset')
            if load_delivery_form.is_valid():
                load_delivery_form.save()

            for files_form in load_files_form.cleaned_data:
                if files_form:
                    files = LoadFiles(files=files_form, key=load)
                    files.save()

            print(load_pickup_form)

            messages.success(request, "Driver Has Been Added Successfully!")
            return redirect('loads:load.all')
    else:
        load_form = LoadForm()
        load_drivers_form = LoadDriversForm()
        load_delivery_form = LoadDeliveryFormset(prefix='load_delivery_formset')
        load_pickup_form = LoadPickupFormset(prefix='load_pickup_formset')
        load_files_form = LoadFilesForm()

    context = {
        'load_form': load_form,
        "load_drivers_form": load_drivers_form,
        'load_delivery_form': load_delivery_form,
        'load_pickup_form': load_pickup_form,
        'load_files_form': load_files_form,
    }
    return render(request, 'loads/loads-add.html', context)



@login_required
def load_detail(request, pk):
    load = Loads.objects.get(id=pk)
    is_late, time_difference = load.is_late()

    # Calculate the hours and minutes from the time difference
    hours = time_difference

    deliveries = LoadDelivery.objects.filter(load=load)
    pickups = LoadPickup.objects.filter(load=load)
    files = LoadFiles.objects.filter(key=load)
    drivers = LoadDrivers.objects.filter(load_key=load)

    context = {
        'load': load,
        'is_late': is_late,
        'hours': hours,

        'deliveries': deliveries,
        'pickups': pickups,
        'files': files,
        'drivers': drivers,
    }
    
    return render(request, 'loads/loads-profile.html', context)


# @login_required
# def show_all_loads(request):
#     loads = Loads.objects.all().order_by('-date_created')
# # Create a Paginator object with a specified number of items per page
#     paginator = Paginator(loads, 10)  # Show 10 loads per page

#     # Get the current page number from the request's GET parameters
#     page_number = request.GET.get('page')

#     # Get the Page object for the requested page number
#     page_obj = paginator.get_page(page_number)


#     # deliveries = LoadDelivery.objects.filter(load__in=loads)
#     context = {
#         'page_obj': page_obj,
#         # 'loads': loads,
#     }
#     return render(request, 'loads/loads-all.html', context)


# @login_required
# def load_list(request):
#     load_manager = Loads.objects
#     # Apply filters based on query parameters or any other conditions
#     loads = load_manager.get_loads(user=request.user, include_all=True)
#     # Or use other methods like load_manager.get_in_transit_loads(), load_manager.get_delivered_loads(), etc.
#     # Configure pagination
#     paginator = Paginator(loads, per_page=10)  # Specify the number of items per page
#     page_number = request.GET.get('page')  # Get the current page number from the query parameters
#     page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

#     # Pass the Page object to the template
#     context = {'page_obj': page_obj}
#     return render(request, 'loads/loads-all-user.html', context)
@login_required
def load_list(request):
    load_manager = Loads.objects
    # user = request.user

    # Get the status filter value from the query parameters
    status = request.GET.get('trailer')
    user = request.GET.get('user')

    # Apply filters based on query parameters or any other conditions
    loads = load_manager.get_loads(user=user, include_all=True)

    if status:
        loads = loads.filter(truck=status)

    # Configure pagination
    paginator = Paginator(loads, per_page=10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, "user":user}
    return render(request, 'loads/loads-all.html', context)
    
import requests
from rest_framework import serializers, views, response

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiZXJub3JlIiwiYSI6ImNsZ2Y1bXR3ODAxNjcza2xjd2h3b2k5ZmEifQ.18V-Hc5DTZpLgjWHTyhLfQ'


class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class SearchPlacesView(views.APIView):
    def get(self, request):
        # query = request.query_params.get('query', '')
        # if len(query) < 3:
        #     return response.Response([])

        # url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json'
        # params = {
        #     'access_token': MAPBOX_ACCESS_TOKEN,
        #     'types': 'address,postcode',
        #     'limit': 10,
        #     'autocomplete': True,
        #     'country': 'us',
        # }
        # response = requests.get(url, params=params)
        # data = response.json()
        # places = [
        #     {
        #         'name': place['place_name'],
        #         'latitude': place['center'][1],
        #         'longitude': place['center'][0],
        #     }
        #     for place in data['features']
        # ]
        # serializer = PlaceSerializer(places, many=True)
        return "gio"

# import requests
# from django.http import JsonResponse

# def address_search(request):

#     if request.method == 'GET' and request.is_ajax():
#         address = request.GET.get('address')
#         response = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + address + '.json?access_token=pk.eyJ1IjoiZXJub3JlIiwiYSI6ImNsZnZlZ20zNzA2aW8zcW8zZ2I5bmhlZzEifQ.F6eFUPq9fipxwy1cp2Qzeg')
#         response_json = response.json()
#         features = response_json['features']
#         return JsonResponse({'features': features})
#     else:
#         return render(request, 'loads/loads-add.html')
=======
from django.shortcuts import render, redirect
from loads.models import Loads, LoadFiles, LoadDrivers
from loads.forms import LoadForm, LoadFormUpload, LoadDriversForm, BookFormSet
from django.contrib import messages
# Create your views here.

def create_load_view(request):
    if request.method == "POST":
        load_form = LoadForm(request.POST)
        # load_drivers = LoadDriversForm(request.POST)
        load_file_form = LoadFormUpload(request.FILES)
        load_files = request.FILES.getlist("files")
        # GET ALL DRIVERS
        formset = BookFormSet(request.POST, instance=f)
        if (load_form.is_valid() and formset.is_valid()):
            #FORMSETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            f = load_form.save(commit=False)
            f.created_by = request.user
            f.save()
            # formset.load = f
            all_formdriver = formset.save(commit=False)
            all_formdriver.save()
            print(formset.errors)
            for i in load_files:
                LoadFiles.objects.create(key=f, files=i)
                # load_file_form.save()
            messages.success(request, "Load Has Been Added Successfully!")
            return redirect('loads:load.all')
        else:
            messages.error(request, "Required Fields May Not Be Filled")
            print(formset.errors)
    else:
        formset = BookFormSet()
        load_form = LoadForm()
        # load_drivers = LoadDriversForm()
        load_file_form = LoadFormUpload()
    return render(request, "loads/loads-add.html", {"formset":formset, "load_form": load_form, "load_file_form": load_file_form})

#Show all Drivers
def list_load_view(request):
    load_list = Loads.objects.all()
    context = {
        'load_list': load_list,
    }
    return render(request, 'loads/loads-all.html', context)

# def edit_trailer_view(request, id):
#     trailer = Trailer.objects.get(id=id)
#     trailer_form = TrailerForm(request.POST or None, instance = trailer)
#     trailer_files = TrailerFormUpload(request.FILES)
#     add_trailer_file = request.FILES.getlist("files")
#     if trailer_form.is_valid():
#         f = trailer_form.save(commit=False)
#         f.created_by = trailer.created_by
#         f.updated_by = request.user
#         f.save()
#         for i in add_trailer_file:
#             TrailerFiles.objects.create(trailer_files=f, files=i+2)
#         messages.success(request, "Trailer Has Been Edited Successfully!")
#         return redirect('trailer:trailers.all')
#     return render(request, 'trailers/trailers-add.html', {'trailer_form' : trailer_form, 'trailer_files':trailer_files})

# def profile_trailer_view(request, id):
#     tracker = TrailerTracker.objects.filter(pgh_obj_id=id).order_by('-pgh_created_at')
#     trailer = Trailer.objects.get(id=id)
#     trailer_files = TrailerFiles.objects.filter(trailer_files_id=id)
#     # file = FileResponse(open(trailer_files, 'rb'))
#     context = {
#         'trailer': trailer,
#         'trailer_files': trailer_files,
#         'tracker': tracker,
#         # 'file': file,
#     }
#     return render(request, 'trailers/trailers-profile.html', context)
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d

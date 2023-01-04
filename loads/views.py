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
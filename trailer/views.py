from django.shortcuts import render, redirect
from trailer.models import Trailer, TrailerFiles, TrailerTracker
from trailer.forms import TrailerForm, TrailerFormUpload
from django.contrib import messages
from django.http import FileResponse

# Create your views here.

def create_trailer_view(request):
    if request.method == "POST":
        trailer_form = TrailerForm(request.POST)
        trailer_files = TrailerFormUpload(request.FILES)
        trailer_file = request.FILES.getlist("files")
        if trailer_form.is_valid():
            f = trailer_form.save(commit=False)
            f.created_by = request.user
            f.save()
            for i in trailer_file:
                TrailerFiles.objects.create(trailer_files=f, files=i)
            messages.success(request, "Trailer Has Been Added Successfully!")
            return redirect('trailer:trailers.all')
        else:
            print(TrailerForm.errors)
    else:
        trailer_form = TrailerForm()
        trailer_files = TrailerFormUpload()
    return render(request, "trailers/trailers-add.html", {"trailer_form": trailer_form, "trailer_files": trailer_files})

#Show all Drivers
def list_trailer_view(request):
    trailer_list = Trailer.objects.all().order_by('-date_created').values()
    context = {
        'trailer_list': trailer_list,
    }
    return render(request, 'trailers/trailers-all.html', context)

def edit_trailer_view(request, id):
    trailer = Trailer.objects.get(id=id)
    trailer_form = TrailerForm(request.POST or None, instance = trailer)
    trailer_files = TrailerFormUpload(request.FILES)
    add_trailer_file = request.FILES.getlist("files")
    if trailer_form.is_valid():
        f = trailer_form.save(commit=False)
        f.created_by = trailer.created_by
        f.updated_by = request.user
        f.save()
        for i in add_trailer_file:
            TrailerFiles.objects.create(trailer_files=f, files=i+2)
        messages.success(request, "Trailer Has Been Edited Successfully!")
        return redirect('trailer:trailers.all')
    return render(request, 'trailers/trailers-add.html', {'trailer_form' : trailer_form, 'trailer_files':trailer_files})

def profile_trailer_view(request, id):
    tracker = TrailerTracker.objects.filter(pgh_obj_id=id).order_by('-pgh_created_at')
    trailer = Trailer.objects.get(id=id)
    trailer_files = TrailerFiles.objects.filter(trailer_files_id=id)
    # file = FileResponse(open(trailer_files, 'rb'))
    context = {
        'trailer': trailer,
        'trailer_files': trailer_files,
        'tracker': tracker,
        # 'file': file,
    }
    return render(request, 'trailers/trailers-profile.html', context)
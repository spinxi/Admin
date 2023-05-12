from drivers.views import *
from . import views
from django.urls import path

app_name = 'drivers'

urlpatterns = [
    #Add
    path("add/", view = create_driver_view, name="drivers.add"),
    #Datatable
    path("", view = list_driver_view, name="drivers.all"),
    #Edit
    path("edit/<int:driver_id>/", view = edit_driver_view, name="drivers.edit"),
    #Show prifile
    path('<int:id>/', view = profile_driver_view, name='drivers.profile'),
]
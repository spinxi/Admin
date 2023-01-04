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
    path("edit/<int:id>/", view = edit_driver_view, name="drivers.edit"),
    #Delete
    path("delete/<int:id>/", view = delete_driver_view, name="drivers.delete"),
    #Show prifile
    path('<int:id>/', view = profile_driver_view, name='drivers.profile'),
]
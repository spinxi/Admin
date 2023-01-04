from .views import *
from django.urls import path

app_name = 'trucks'

urlpatterns = [
    #Add
    path("add/", view = create_truck_view, name="trucks.add"),
    #Datatable
    path("list/", view = list_truck_view, name="trucks.all"),
    #Edit
    path("edit/<int:id>/", view = edit_truck_view, name="trucks.edit"),
]
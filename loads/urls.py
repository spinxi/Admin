from loads.views import *
from django.urls import path

app_name = 'loads'

urlpatterns = [
    #Add
    path("add/", view = create_load_view, name="load.add"),
    #Datatable
    path("", view = list_load_view, name="load.all"),
    # #Edit
    # path("edit/<int:id>/", view = edit_truck_view, name="trucks.edit"),
    # #Delete
    # path("delete/<int:id>/", view = delete_truck_view, name="trucks.delete"),
]
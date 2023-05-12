<<<<<<< HEAD
from loads.views import create_load,load_list,  load_detail, SearchPlacesView
from django.urls import path, include
from rest_framework import routers

app_name = 'loads'


urlpatterns = [
    path('create_load/', create_load, name="load.add"),
    path('', load_list, name="load.all"),
    path('api/search-places/', SearchPlacesView.as_view()),
    path('<int:pk>/', load_detail, name='load_detail'),
=======
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
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d
]
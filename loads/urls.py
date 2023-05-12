from loads.views import create_load,load_list,  load_detail, SearchPlacesView
from django.urls import path, include
from rest_framework import routers

app_name = 'loads'


urlpatterns = [
    path('create_load/', create_load, name="load.add"),
    path('', load_list, name="load.all"),
    path('api/search-places/', SearchPlacesView.as_view()),
    path('<int:pk>/', load_detail, name='load_detail'),
]
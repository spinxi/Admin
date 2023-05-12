from trailer.views import *
from . import views
from django.urls import path

app_name = 'trailer'

urlpatterns = [
    #Add
    path("add/", view = create_trailer_view, name="trailers.add"),
    #Datatable
    path("", view = list_trailer_view, name="trailers.all"),
    # #Edit
    path("edit/<int:id>/", view = edit_trailer_view, name="trailers.edit"),
    #Profile
    path("profile/<int:id>/", view = profile_trailer_view, name="trailers.profile"),
]


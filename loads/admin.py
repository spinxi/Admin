from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin


from .models import LoadDrivers

@admin.register(LoadDrivers)
class Client_Log(admin.ModelAdmin):
    pass


# @admin.register(Clients)
# class Clients(admin.ModelAdmin):
#     search_fields = ('first_name', 'last_name', 'dod_id')
#     list_display = ('last_name', 'first_name', 'middle_initial', 'dod_id')
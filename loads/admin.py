from django.contrib import admin

# Register your models here.
<<<<<<< HEAD

from django.contrib.auth.admin import UserAdmin


from .models import LoadDrivers

@admin.register(LoadDrivers)
class Client_Log(admin.ModelAdmin):
    pass


# @admin.register(Clients)
# class Clients(admin.ModelAdmin):
#     search_fields = ('first_name', 'last_name', 'dod_id')
#     list_display = ('last_name', 'first_name', 'middle_initial', 'dod_id')
=======
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d

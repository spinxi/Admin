from django.contrib import admin
# from .models import DriversFiles
# # Register your models here.
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin


from .models import Driver

@admin.register(Driver)
class Client_Log(admin.ModelAdmin):
    pass
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_string', 'action_time', 'object_id')
    actions = None

    def get_string(self, obj):
        return str(obj)

    search_fields = ['=user__username', ]
    fieldsets = [
        (None, {'fields':()}), 
        ]

    def __init__(self, *args, **kwargs):
        super(LogEntryAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = None

admin.site.register(admin.models.LogEntry, LogEntryAdmin)
=======
# admin.site.register(DriversFiles)

>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d

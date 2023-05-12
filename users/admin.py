from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('is_driver', 'is_accountant', 'is_dispatcher')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_driver', 'is_accountant', 'is_dispatcher', 'is_active', 'groups', 'user_permissions'),
        }),
    )

    list_display = ['email', 'is_active', 'date_joined', 'last_login', 'is_driver', 'is_accountant', 'is_dispatcher']
    list_filter = ['is_active', 'is_driver', 'is_accountant', 'is_dispatcher', 'groups']
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
=======

# Register your models here.
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d

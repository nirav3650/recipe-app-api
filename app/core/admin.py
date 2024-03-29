from django.contrib import admin
from core import models
# Register your models here.
from django.contrib.auth.admin import UserAdmin as Baseuseradmin
from django.utils.translation import gettext as _
class UserAdmin(Baseuseradmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
    (None, {
        'classes': ("wide", ),
        "fields": ("email", "password1", "password2")
    }),
    )
admin.site.register(models.User, UserAdmin)
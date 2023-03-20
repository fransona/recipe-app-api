""""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Premissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )

            }
        ),
        (_('Important dates listed'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


# registering a user model with customized page with ordering and listing.
# If not mentioned  UserAdmin created.
# It will have only basic create, read, update operations
admin.site.register(models.User, UserAdmin)

# register the recipe model with default admin class
# Unlike user model we don't have customized admin class for recipe
admin.site.register(models.Recipe)

admin.site.register(models.Tag)

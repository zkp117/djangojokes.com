from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse

from common.admin import DjangoJokesAdmin
from common.utils.admin import append_fields, move_fields, remove_fields

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(DjangoJokesAdmin, UserAdmin):
    model = CustomUser

    # List Attributes
    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    # Fields for editing existing user.
    new_fields = ('dob', 'avatar')

    append_fields(UserAdmin.fieldsets, 'Personal info', new_fields)
    append_fields(UserAdmin.fieldsets, None, ('password_form',))
    move_fields(UserAdmin.fieldsets, 'Personal info', None, ('email',))
    remove_fields(UserAdmin.fieldsets, None, ('password',))

    readonly_fields = ['password_form']

    new_fields = ('email', )
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, None, new_fields)

    # Add optional fields to new 'Optional Fields' section.
    optional_fields = ('first_name', 'last_name', 'dob')
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, 'Optional Fields', optional_fields)

    # Add Save buttons to the top of the change user form
    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)
    
    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

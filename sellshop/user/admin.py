from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# from user.models import BillingAddress


# admin.site.unregister(BaseUserAdmin)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'sex', 'bio', 'image')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)


# @admin.register(BillingAddress)
# class BillingAddressAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email','reference', 'created_at')
#     list_filter = ( 'created_at', )
#     search_fields = ('first_name', )
#     fieldsets = [
#         ('Standard info', {
#             'fields': ('first_name', 'last_name','email','country','town','address','mobile_phone','information','reference', ),
#             'classes': ('collapse',)
#         }),
#         # ('Other', {
#         #     'fields': ('tags', )
#         # }),
#     ]

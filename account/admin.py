from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from account.models import Account, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'manzil', 'max_worker_count', 'worker_count', 'creator',)
    list_display_links = ['name']


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'token', 'phone', 'company', 'filial')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_director', 'is_callcenter'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'company')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'company')


admin.site.register(Account, UserAdmin)
admin.site.unregister(Group)

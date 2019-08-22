from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .models import AssemblyWarehouse,CityWarehouse,SubWarehouse,TotalSubWarehouse,TotalCityWarehouse

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('User type'), {'fields': ('is_aw_manager', 'is_cw_manager', 'is_sw_manager', 'is_aw_executive','is_cw_executive','is_sw_executive','is_aw_transport', 'is_cw_transport', 'is_sw_transport')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(AssemblyWarehouse)
admin.site.register(CityWarehouse)
admin.site.register(SubWarehouse)

admin.site.register(TotalSubWarehouse)
admin.site.register(TotalCityWarehouse)
from accounts.models import Account
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display        = ('email','first_name','last_name', 'username','date_joined','last_login','is_active')
    list_display_links  = ('email','first_name','last_name')
    search_fields       = ('email','username')
    readonly_fields     = ('date_joined','last_login') # can't be altered
    
    ordering            = ('-date_joined',) # displays in order of recently joined

    # required
    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()
admin.site.register(Account,AccountAdmin)

from django.contrib import admin
from .models import Product, SERVICES
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)


class PRODUCTAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    list_display_links = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    readonly_fields = ('CREATED_AT', 'UPDATED_AT')


class SERVICESAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    list_display_links = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')
    readonly_fields = ('CREATED_AT', 'UPDATED_AT')


# Register your models here.
admin.site.register(Product, PRODUCTAdmin)
admin.site.register(SERVICES, SERVICESAdmin)

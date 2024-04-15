from django.contrib import admin
from .models import Product, SERVICES


class PRODUCTAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')


class SERVICESAdmin(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'SLUG', 'CREATED_AT', 'UPDATED_AT')


# Register your models here.
admin.site.register(Product, PRODUCTAdmin)
admin.site.register(SERVICES, SERVICESAdmin)

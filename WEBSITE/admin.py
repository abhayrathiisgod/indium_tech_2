from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import ContactForm, ContactInfo, PageContent, Banner_Images


class ContactFromAdmin(admin.ModelAdmin):
   # actions = None
    list_display = ('Name', 'Email', 'Subject', 'Created_at')
    list_filter = ('Name', 'Email', 'Subject', 'Created_at')
    list_display_links = ('Name', 'Email', 'Subject', 'Created_at')
    readonly_fields = ('Created_at', 'Updated_at')


class Banner_ImagesAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Banner', 'Title', 'Description',
                    'Created_at', 'Updated_at')
    list_filter = ('Created_at', 'Updated_at')
    list_display_links = ('Banner', 'Title', 'Description',
                          'Created_at', 'Updated_at')

    def has_add_permission(self, request: HttpRequest) -> bool:
        if Banner_Images.objects.count() >= 5:
            return False

        return super().has_add_permission(request)


class ContactInfoAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Email', 'Phone', 'Address', 'Updated_at')
    list_display_links = ('Email', 'Phone', 'Address', 'Updated_at')
    readonly_fields = ('Created_at', 'Updated_at')

    def has_add_permission(self, request):

        if ContactInfo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class PageContentAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Page_Type', 'Page_Title', 'Created_at', 'Updated_at')
    list_filter = ('Created_at', 'Updated_at')
    list_display_links = ('Page_Type', 'Page_Title',
                          'Created_at', 'Updated_at')
    readonly_fields = ('Created_at', 'Updated_at')

    def has_add_permission(self, request: HttpRequest) -> bool:
        if PageContent.objects.count() >= 5:
            return False
        return super().has_add_permission(request)


# Register your models here.

admin.site.register(ContactForm, ContactFromAdmin)
admin.site.register(Banner_Images, Banner_ImagesAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(PageContent, PageContentAdmin)

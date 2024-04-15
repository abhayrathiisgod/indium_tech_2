from django.contrib import admin
from .models import ContactForm, ContactInfo, PageContent, Banner_Images


class ContactFromAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Subject', 'Created_at')
    list_filter = ('Name', 'Email', 'Subject', 'Created_at')


class Banner_ImagesAdmin(admin.ModelAdmin):
    list_display = ('Banner', 'Title', 'Description',
                    'Created_at', 'Updated_at')
    list_filter = ('Created_at', 'Updated_at')


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('Email', 'Phone', 'Address', 'Updated_at')


class PageContentAdmin(admin.ModelAdmin):
    list_display = ('Page_Title', 'Created_at', 'Updated_at')
    list_filter = ('Created_at', 'Updated_at')

# Register your models here.


admin.site.register(ContactForm, ContactFromAdmin)
admin.site.register(Banner_Images, Banner_ImagesAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(PageContent, PageContentAdmin)

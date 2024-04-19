from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import ContactForm, ContactInfo, PageContent, Banner_Images


class ContactFromAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Name', 'Email', 'Subject', 'Created_at')
    list_filter = ('Name', 'Email', 'Subject', 'Created_at')
    list_display_links = ('Name', 'Email', 'Subject', 'Created_at')


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


# class ContactInfoForm(forms.ModelForm):
#     Facebook_link = forms.URLField(
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     Instagram_link = forms.URLField(
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     X_link = forms.URLField(
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     Youtube_link = forms.URLField(
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     Linkedin_link = forms.URLField(
#         widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#     class Meta:
#         model = ContactInfo
#         fields = ['Facebook_link', 'Instagram_link',
#                   'X_link', 'Youtube_link', 'Linkedin_link']


class ContactInfoAdmin(admin.ModelAdmin):
    actions = None
    # form = ContactInfoForm
    list_display = ('Email', 'Phone', 'Address', 'Updated_at')
    list_display_links = ('Email', 'Phone', 'Address', 'Updated_at')
    readonly_fields = ('Created_at', 'Updated_at')

    def has_add_permission(self, request: HttpRequest) -> bool:
        if ContactInfo.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def clickable_url(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.Facebook_link, obj.Facebook_link)
    clickable_url.allow_tags = True
    clickable_url.short_description = 'URL'

    # def show_Facebook_link(self, obj):

    #     return 'Currently: < a href = "%s" > %s < /a >' % (obj.Facebook_link)

    # show_Facebook_link.allow_tags = True

    # def change_view(self, request, object_id, form_url='', extra_context=None) -> HttpResponse:

    #     if obj := self.get_object(request, object_id):
    #         extra_context = extra_context or {}
    #         extra_context['currently'] = obj.Facebook_link
    #         extra_context['currently'] = obj.Instagram_link
    #         extra_context['currently'] = obj.X_link
    #         extra_context['currently'] = obj.Youtube_link
    #         extra_context['currently'] = obj.Linkedin_link

    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)


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

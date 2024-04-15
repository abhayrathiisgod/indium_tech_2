from rest_framework import serializers
from .models import ContactForm, ContactInfo, PageContent, Banner_Images


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['Name', 'Email', 'Subject', 'Message']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['Email', 'Phone', 'Address']


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageContent
        fields = ['Page_Type', 'Page_Title', 'Page_Content', 'image']


class Banner_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner_Images
        fields = ['Banner', 'Title', 'Description', 'Image']

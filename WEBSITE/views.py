from django.shortcuts import render
from rest_framework import generics
from .models import ContactForm, ContactInfo, PageContent, Banner_Images
from .serializers import ContactFormSerializer, ContactInfoSerializer, PageContentSerializer, Banner_ImagesSerializer


# Create your views here.


class ContactFormView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class PageContentView(generics.ListAPIView):
    queryset = PageContent.objects.all()
    serializer_class = PageContentSerializer


class Banner_ImagesView(generics.ListAPIView):
    queryset = Banner_Images.objects.all()
    serializer_class = Banner_ImagesSerializer

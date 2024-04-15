from django.urls import path
from .views import ContactFormView, ContactInfoView, PageContentView, Banner_ImagesView

urlpatterns = [
    path('contact_form/', ContactFormView.as_view()),
    path('contact_info/', ContactInfoView.as_view()),
    path('page_content/', PageContentView.as_view()),
    path('banner_images/', Banner_ImagesView.as_view()),
]

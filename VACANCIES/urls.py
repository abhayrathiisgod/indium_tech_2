from django.urls import path
from .views import JobView, HasOpening


urlpatterns = [
    path('carrers/', JobView.as_view()),
    path('carrers/<int:pk>/', JobView.as_view(), name='job-detail'),
    path('has_opening/', HasOpening.as_view()),
]

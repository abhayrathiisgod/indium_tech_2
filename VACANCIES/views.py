from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Jobs
from .serializers import JobsSerializer, HasOpeningSerializer
from rest_framework.response import Response
# Create your views here.


class JobView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class SpecificJobView(generics.RetrieveAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    lookup_field = 'pk'


class HasOpening(APIView):
    def get(self, request, *args, **kwargs):
        has_opening = Jobs.objects.exists()
        data = {'has_opening': has_opening}
        serializer = HasOpeningSerializer(data)
        return Response(serializer.data)

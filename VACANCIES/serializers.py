from rest_framework import serializers
from .models import Jobs, Candidates


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['Id', 'Title', 'Job_name',
                  'is_published', 'Open_date', 'Close_date']


class HasOpeningSerializer(serializers.Serializer):
    has_opening = serializers.BooleanField()

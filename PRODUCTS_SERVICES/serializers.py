from rest_framework import serializers
from .models import Product, SERVICES


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['NAME', 'SLUG', 'ICON', 'SHORT_DESCRIPTION']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SERVICES
        fields = ['NAME', 'SLUG', 'ICON', 'IMAGE', 'SHORT_DESCRIPTION']

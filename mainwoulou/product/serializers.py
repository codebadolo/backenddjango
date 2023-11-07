from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Product

from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = "__all__"


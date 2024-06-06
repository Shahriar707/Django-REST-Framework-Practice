from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

# def validate_title(value):
#     queryset = Product.objects.filter(title__iexact=value)
#     if queryset.exists():
#         raise serializers.ValidationError(f"{value} is already taken as product name")
#     return value 

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value 

unique_title_name = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
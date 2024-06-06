from django.shortcuts import render
from django.http import JsonResponse 
import json 
from products.models import Product
from django.forms.models import model_to_dict 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from products.serializers import ProductSerializer 

# Create your views here.
"""
DRF API View 
"""
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
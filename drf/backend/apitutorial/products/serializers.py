from rest_framework import serializers 
from rest_framework.reverse import reverse 
from api.serializers import UserPublicSerializer
from .models import Product
from . import validators

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(read_only=True)
    
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    discount = serializers.SerializerMethodField(read_only=True) 
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name='product-detail', lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validators.unique_title_name, validators.validate_title_no_hello])
    body = serializers.CharField(source='content')
    class Meta:
        model = Product 
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'discount',
            'public',
            'path',
        ]
        
    def get_user_data(self, obj):
        username = obj.user.username 
        
        return username 
        
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)
        
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None 
        if not isinstance(obj, Product):
            return None 
        return obj.get_discount()     
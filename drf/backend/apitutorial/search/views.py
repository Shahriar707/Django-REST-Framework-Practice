from rest_framework import generics
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer
from . import client 

# Create your views here.

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None 
        if self.request.user.is_authenticated:
            user = self.request.user.username 
        public = str(self.request.GET.get('public')) != "0"
        query = self.request.GET.get('q')
        tag = self.request.GET.get('tag') or None 
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user 
            results = qs.search(q, user=user)
        
        return results 
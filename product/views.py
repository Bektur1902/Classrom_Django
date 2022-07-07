from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from .models import Product


# Create your views here.


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


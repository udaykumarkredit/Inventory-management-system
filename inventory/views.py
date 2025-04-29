from rest_framework import viewsets
from .models import Supplier,Category,Product,Warehouse,StockMovement
from .serializers import StockMovementSerializer,SupplierSerializer,WarehouseSerilaizer,ProductSerializer,CategorySerializer

# Create your views here.
class SupplierViewSet(viewsets.ModelViewSet):
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class WarehouseViewSet(viewsets.ModelViewSet):
    queryset=Warehouse.objects.all()
    serializer_class=WarehouseSerilaizer

class StockMovementViewSet(viewsets.ModelViewSet):
    queryset=StockMovement.objects.all()
    serializer_class=StockMovementSerializer
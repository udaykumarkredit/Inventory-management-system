from rest_framework import serializers
from .models import Product, Category, Supplier, StockMovement, Warehouse, StockTypes


# Serializer for Category Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# Serializer for Supplier Model
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


# Serializer for Product Model
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = "__all__"


# Serilaizer for Warehouse model
class WarehouseSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = "__all__"

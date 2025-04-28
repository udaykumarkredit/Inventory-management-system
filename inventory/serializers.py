from rest_framework import serializers
from .models import Product,Category,Supplier,Manufacturer,StockMovement

# Serializer for Category Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

# Serializer for Supplier Model
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'
        
# Serializer for Product Model
class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    supplier=SupplierSerializer()
    
    class Meta:
        model=Product
        fields=["id","name","description","price","category","supplier","stock_quantity","unit_price"]
        
        def create(self,validated_data):
            category_data=validated_data.pop('category')
            supplier_data=validated_data.pop("supplier_data")
            
            category=Category.objects.create(**category_data)
            supplier=Supplier.objects.create(**supplier_data)
            
            product=Product.objects.create(category=category,supplier=supplier,**validated_data)
            return product
        
        def update(self,instance,validated_data):
            category_data=validated_data.pop("category",None)
            supplier_data=validated_data.pop("supplier",None)
            
            if category_data:
                category=instance.category
                instance.category.name=category_data.get("name",category.name)
                instance.category.save()
                
            if supplier_data:
                supplier=instance.supplier
                instance.supplier.name=supplier_data.get("name",supplier.name)
                instance.supplier.save()
            
            
        

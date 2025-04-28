from rest_framework import serializers
from .models import Product, Category, Supplier, Manufacturer, StockMovement, StockTypes


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
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "supplier",
            "stock_quantity",
            "unit_price",
            "manufactured_date",
            "expiry_date",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        supplier_data = validated_data.pop("supplier_data")

        category = Category.objects.create(**category_data)
        supplier = Supplier.objects.create(**supplier_data)

        product = Product.objects.create(
            category=category, supplier=supplier, **validated_data
        )
        return product

    def update(self, instance, validated_data):
        category_data = validated_data.pop("category", None)
        supplier_data = validated_data.pop("supplier", None)

        if category_data:
            category = instance.category
            instance.category.name = category_data.get("name", category.name)
            instance.category.save()

        if supplier_data:
            supplier = instance.supplier
            instance.supplier.name = supplier_data.get("name", supplier.name)
            instance.supplier.save()

        instance.name = validated_data.get("name", instance.name)
        instance.unit_price = validated_data.get("unit_price", instance.unit_price)
        instance.damaged_products = validated_data.get(
            "damaged_products", instance.damaged_products
        )
        instance.manufactured_date = validated_data.get(
            "unit_price", instance.manufactured_date
        )
        instance.expiry_date = validated_data.get("expiry_date", instance.expiry_date)
        instance.save()
        return instance


# Serializer for stockmovement model
class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = ["id", "product", "movement_type", "quantity", "reason", "timestamp"]

    def create(self, validated_data):
        product_data = validated_data.pop("product")
        product = Product.objects.get(id=product_data["id"])

        movement = StockMovement.objects.create(product=product, **validated_data)

        # update stock_quantity after movement
        if validated_data["movement_type"] == StockTypes.IN:
            product.stock_quantity += validated_data["quantity"]
        else:
            if product.stock_quantity >= validated_data["quantity"]:
                product.stock_quantity -= validated_data["quantity"]
            else:
                raise serializers.ValidationError(
                    f"Not enough stock to perform 'stock out' operation. "
                )
        product.save()
        return movement

from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    stock_quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(
        "Supplier", on_delete=models.CASCADE, related_name="products"
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    damaged_products = models.PositiveIntegerField(default=0)
    # manufactured_by = models.ForeignKey(
    #     "Manufacturer", on_delete=models.PROTECT, related_name="products"
    # )
    manufactured_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-manufatuctured by {self.manufactured_by}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=True)
    phone=models.CharField(max_length=20,blank=True)
    address=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


# class Manufacturer(models.Model):
#     name = (models.CharField(max_length=100),)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
class StockTypes:
    IN="Stock In",
    OUT='Stock Out'
    
    choices=(
        ("IN","Stock In"),
        ("OUT","Stock Out")
    )
    
class Warehouse(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=255)
    capacity=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class StockMovement(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    movement_type=models.CharField(max_length=3,choices=StockTypes.choices)
    timestamp=models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveIntegerField()
    reason=models.TextField(blank=True)
    
    class Meta:
        ordering=['-timestamp']
    

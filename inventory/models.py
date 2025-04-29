from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    stock_quantity = models.PositiveIntegerField(default=0)
    supplier = models.ManyToManyField(
        "Supplier", related_name="products"
    )
    warehouse = models.ManyToManyField(
        "Warehouse", related_name="products"
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StockTypes:
    IN = ("Stock In",)
    OUT = "Stock Out"

    choices = (("IN", "Stock In"), ("OUT", "Stock Out"))


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, default=1)
    movement_type = models.CharField(max_length=3, choices=StockTypes.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    reason = models.TextField(blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def save(self, *args, **kwargs):
        if self.movement_type == StockTypes.IN:
            self.product.stock_quantity += self.quantity
        elif self.movement_type == StockTypes.OUT:
            if self.quantity <= self.product.stock_quantity:
                self.product.stock_quantity -= self.quantity
            else:
                raise ValueError("not enough stock!!")
        else:
            raise ValueError("Invalid Movement Type")

        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name

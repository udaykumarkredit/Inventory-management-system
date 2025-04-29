from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet,ProductViewSet,CategoryViewSet,WarehouseViewSet,StockMovementViewSet

router=DefaultRouter()
router.register(r"suppliers",SupplierViewSet)
router.register(r"categories",CategoryViewSet)
router.register(r"product",ProductViewSet)
router.register(r"warehouse",WarehouseViewSet)
router.register(r"stock-movement",StockMovementViewSet)

urlpatterns=[
    path("",include(router.urls))
]

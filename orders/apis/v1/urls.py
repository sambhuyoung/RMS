from .views import MenuItemViewSet, TableViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet, basename='menuitem')
router.register(r'tables', TableViewSet, basename='table')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
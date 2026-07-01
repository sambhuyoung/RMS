from .views import MenuItemViewSet, TableViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet, basename='menuitem')
router.register(r'tables', TableViewSet, basename='table')

urlpatterns = router.urls
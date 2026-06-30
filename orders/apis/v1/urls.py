from .views import MenuItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet, basename='menuitem')
urlpatterns = router.urls
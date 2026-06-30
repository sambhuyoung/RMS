from .serializers import MenuItemSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from orders.models import MenuItem

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

from .serializers import MenuItemSerializer, TableSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from orders.models import MenuItem , Table


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

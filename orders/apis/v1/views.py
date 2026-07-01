from django.db.migrations import serializer

from .serializers import MenuItemSerializer, TableSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from orders.models import MenuItem, Table
from rest_framework.response import Response
from rest_framework import status


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    @action(detail=True, methods=['get'])
    def check_reservation(self, request, pk=None):
        try:
            table = self.queryset.get(pk=pk)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(data = {'is_reserved': table.is_reserved})

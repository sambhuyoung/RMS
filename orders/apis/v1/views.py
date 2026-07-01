from django.db.migrations import serializer

from rest_framework import viewsets
from rest_framework.decorators import action
from orders.models import MenuItem, Table, Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuItemSerializer, TableSerializer, CategorySerializer
from rest_framework.pagination import LimitOffsetPagination



class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # For pagination
    pagination_class = LimitOffsetPagination # There won't be any difference until write on ULR '?limit=10
    # view 'https://www.django-rest-framework.org/api-guide/pagination/'



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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

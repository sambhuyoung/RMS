from django.db.migrations import serializer

from rest_framework import viewsets
from rest_framework.decorators import action
from orders.models import MenuItem, Table, Category
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuItemSerializer, TableSerializer, CategorySerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated




class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # For pagination
    pagination_class = LimitOffsetPagination # There won't be any difference until write on ULR '?limit=10, look at 'https://www.django-rest-framework.org/api-guide/pagination/'
    # For authentication
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     name = self.request.query_params.get('name') # will get data (paramenter) from the URL which is added to search.
    #
    #     return MenuItem.objects.filter(name__icontains=name)name

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            # नाम भएको बेला मात्र फिल्टर गर्ने
            queryset = MenuItem.objects.filter(name__icontains=name)
        else:
            # नाम नपठाए सबै आइटमहरू देखाइदिने
            queryset = MenuItem.objects.all()

        # More filters

        # price_lt = self.request.query_params.get("price_lt", None)
        # if price_lt is not None:
        #     queryset = MenuItem.objects.filter(price_lt__icontains=price_lt)
        # else:
        #     queryset = MenuItem.objects.all()
        #
        #     # २. यदि क्याटेगोरी पठाइएको छ भने क्याटेगोरीले फिल्टर गर्ने
        #     if category is not None:
        #         queryset = queryset.filter(
        #             category__icontains=category
        #         )  # वा category=category
        #
        return queryset

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

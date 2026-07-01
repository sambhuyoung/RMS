from django.contrib.admin import action
from rest_framework import serializers, status
from rest_framework.response import Response
from orders.models import MenuItem, Table
from rest_framework.decorators import action

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

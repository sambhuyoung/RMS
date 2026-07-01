from rest_framework import serializers
from orders.models import MenuItem, Table, Category


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    # also give Items making it read only not modifiyable.
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
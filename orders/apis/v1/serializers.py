from rest_framework import serializers
from orders.models import MenuItem, Table, Category, KitchenStation


class KitchenStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenStation
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    station = KitchenStationSerializer()
    class Meta:
        model = MenuItem
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    # also give Items making it read only not chageable.
    #items = MenuItemSerializer(many=True, read_only=True)

    # giving different name than in relation name inbetween MenuItems and Category.
    menuitems = MenuItemSerializer(source='items', many = True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
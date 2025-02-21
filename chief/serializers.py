from rest_framework import serializers
from .models import Desktop, Description, Characteristic, Favorites, Brand, Model, AllCars, Filters


class DesktopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desktop
        fields = '__all__'


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class CharacteristicSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class AllCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCars
        fields = '__all__'

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = '__all__'
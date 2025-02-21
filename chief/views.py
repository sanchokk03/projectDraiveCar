from dal import autocomplete
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Desktop, Description, Characteristic, Favorites, Model, AllCars, Filters
from .serializers import DesktopSerializer, DescriptionSerializer, CharacteristicSetSerializer, FavoritesSerializer, AllCarsSerializer, FilterSerializer


@api_view(['GET'])
def desktop_list(request):
    desktop = Desktop.objects.all()
    serializer = DesktopSerializer(desktop, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def description_list(request):
    description = Description.objects.all()
    serializer = DescriptionSerializer(description, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def characteristic_list(request):
    characteristic = Characteristic.objects.all()
    serializer = CharacteristicSetSerializer(characteristic, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def favorite_list(request):
    favorite = Favorites.objects.all()
    serializer = FavoritesSerializer(favorite, many=True)
    return Response(serializer.data)

class ModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Model.objects.all()

        brand_id = self.forwarded.get('brand', None)
        if brand_id:
            qs = qs.filter(brand_id=brand_id)

        return qs


@api_view(['GET'])
def all_cars_list(request):
    all_cars = AllCars.objects.all()
    serializer = AllCarsSerializer(all_cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_list(request):
    filter = Filters.objects.all()
    serializer = FilterSerializer(filter, many=True)
    return Response(serializer.data)
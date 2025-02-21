from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import desktop_list, description_list, characteristic_list, favorite_list, ModelAutocomplete, all_cars_list, filter_list

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('desktop/', desktop_list),
    path('description/', description_list),
    path('characteristic/', characteristic_list),
    path('favorite/', favorite_list),
    path('model-autocomplete/', ModelAutocomplete.as_view(), name='model-autocomplete'),
    path('all-cars/', all_cars_list),
    path('filter/', filter_list),

]


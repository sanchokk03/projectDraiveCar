from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # Генерация схемы OpenAPI (JSON)
    path("schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    # Redoc
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .generator import HttpAndHttpsSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(title="Beauty Web", default_version="v1"),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=HttpAndHttpsSchemaGenerator,
)

swagger_patterns = [
    re_path(r"^doc(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json", ),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui", ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

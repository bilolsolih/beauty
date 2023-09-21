from django.contrib import admin
from django.urls import path, include

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('about/', include('apps.about.urls', namespace='about')),
]

urlpatterns += swagger_patterns

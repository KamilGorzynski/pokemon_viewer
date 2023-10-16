import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .views import healthcheck_view

urlpatterns = [
    path("healthcheck/", healthcheck_view),
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('pokemons/', include('pokemons.urls'))
]

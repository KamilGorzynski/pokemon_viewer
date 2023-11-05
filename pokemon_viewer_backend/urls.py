import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .views import healthcheck_view
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("healthcheck/", healthcheck_view),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("pokemons/", include("pokemons.urls")),
]

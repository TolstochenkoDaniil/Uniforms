from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_auth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('api/v1/', include('forms.urls')),
]

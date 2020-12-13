from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_auth.urls')),
    path('users/', include('forms.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]

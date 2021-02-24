from django.urls import path

from . import views


urlpatterns = [
    path('<user_id>/form', views.FormViewSet.as_view({
            'get':'retrieve',
            'post':'create'
        })
    ),
    path('forms/<discipline>/list', views.FormViewSet.as_view({'get':'list'}))
]
from django.urls import path

from .views import (
    resource_create,
    resource_delete,
    resource_detail,
    resource_list,
    resource_update,
)

urlpatterns = [
    path('', resource_list, name='resource_list'),
    path('resources/<int:pk>/', resource_detail, name='resource_detail'),
    path('resources/new/', resource_create, name='resource_create'),
    path('resources/<int:pk>/edit/', resource_update, name='resource_update'),
    path('resources/<int:pk>/delete/', resource_delete, name='resource_delete'),
]

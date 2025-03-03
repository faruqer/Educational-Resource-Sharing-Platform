from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ResourceViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='api-category')
router.register('resources', ResourceViewSet, basename='api-resource')

urlpatterns = router.urls

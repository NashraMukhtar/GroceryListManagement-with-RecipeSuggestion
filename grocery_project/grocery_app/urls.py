from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
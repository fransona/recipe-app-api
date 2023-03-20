"""
URL mappings for the recipe app
"""

from django.urls import (
    path,
    include,
)

# Automatically creats routes to all the options available
# as we use modelviewset, it has endpoints for all CURD options
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)

# app name used in the reverse lookup of url
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]

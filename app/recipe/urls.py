from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# Default router generates the association with viewsets and the urls

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_kin_media import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'media', views.MediaViewSet,basename="media")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('media/', include(router.urls)),
]
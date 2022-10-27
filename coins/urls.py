from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CoinViewset

router = DefaultRouter()

router.register('coins', CoinViewset, basename='coins')

urlpatterns = [
    path('', include(router.urls))
]
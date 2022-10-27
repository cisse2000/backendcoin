from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CoinSerializer

from .models import Coin

class CoinViewset(viewsets.ModelViewSet):
    coins = Coin.objects.all()
    serializer_class = CoinSerializer

    def get_queryset(self):
        return self.coins
        
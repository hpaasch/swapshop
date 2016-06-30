from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

import json
from main_app.models import Listing
from shop_api.serializers import SwapShopSerializer

class SwapShopListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopSerializer


# class SwapShopDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # pass

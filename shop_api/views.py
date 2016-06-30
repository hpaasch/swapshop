from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

import json
from main_app.models import Listing, Category
from shop_api.serializers import SwapShopListingSerializer, SwapShopCategorySerializer

class SwapShopListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer


class SwapShopCategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(choose_main=None)


class SwapShopCategoryDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(choose_main=None)


class SwapShopSubCategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(choose_main=True)

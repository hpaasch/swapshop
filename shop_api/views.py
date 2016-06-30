from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

import json
from main_app.models import Listing, Category
from shop_api.serializers import SwapShopListingSerializer, SwapShopCategorySerializer


class SwapShopListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer


class SwapShopDetailAPIView(generics.RetrieveUpdateAPIView):
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


class SwapShopCategoryListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer

    def get_queryset(self):
        main_cat_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(pick_category__choose_main=main_cat_id)


class SwapShopSubCatAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.exclude(choose_main=None)


class SwapShopSubCatDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer


class SwapShopSubCatListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer

    def get_queryset(self):
        sub_cat_id = self.kwargs.get('pk')
        return Listing.objects.filter(pick_category=sub_cat_id)

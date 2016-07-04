from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from shop_api.permissions import IsOwnerOrReadOnly
from django.core.urlresolvers import reverse, reverse_lazy


import json
from main_app.models import Listing, Category
from shop_api.serializers import SwapShopListingSerializer, SwapShopCategorySerializer, CreateUserSerializer


class SwapShopListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SwapShopDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class SwapShopCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(choose_main=None)


class SwapShopCategoryCreateAPIView(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.filter(choose_main=None)
        else:
            # return HttpResponse('es no bueno')
            return HttpResponseRedirect(reverse_lazy('/api/main_categories/'))
            # this return gives an error.

class SwapShopCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(choose_main=None)


class SwapShopCategoryListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer

    def get_queryset(self):
        main_cat_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(pick_category__choose_main=main_cat_id)


class SwapShopSubCatAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        return Category.objects.exclude(choose_main=None)


class SwapShopSubCatCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.exclude(choose_main=None)
        else:
            # return HttpResponse('es no bueno')
            return HttpResponseRedirect(reverse_lazy('/api/sub_categories/'))
            # this return gives an error.


class SwapShopSubCatDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = SwapShopCategorySerializer


class SwapShopSubCatListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = SwapShopListingSerializer

    def get_queryset(self):
        sub_cat_id = self.kwargs.get('pk')
        return Listing.objects.filter(pick_category=sub_cat_id)


class SwapShopRegisterAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

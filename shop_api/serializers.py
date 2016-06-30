from rest_framework import serializers
from main_app.models import Listing, Category

class SwapShopListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'photo', 'city', 'seller', 'pick_category')


class SwapShopCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'new_category', 'choose_main')

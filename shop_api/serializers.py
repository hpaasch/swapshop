from rest_framework import serializers
from main_app.models import Listing

class SwapShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'photo', 'city', 'seller', 'pick_category')

        

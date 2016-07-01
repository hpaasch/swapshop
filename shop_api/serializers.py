from rest_framework import serializers
from main_app.models import Listing, Category
from django.contrib.auth.models import User


class SwapShopListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('id', 'title', 'description', 'price', 'photo', 'city', 'seller', 'pick_category')


class SwapShopCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'new_category', 'choose_main')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

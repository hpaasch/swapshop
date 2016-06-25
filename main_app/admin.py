from django.contrib import admin
from main_app.models import Listing, Category, TraderProfile, Location


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'pick_category']
    search_fields = ['title', 'description']

admin.site.register(Listing)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['new_category', 'choose_main']
    search_fields = ['new_category', 'choose_main']

    class Meta:
        ordering = ['choose_main']

admin.site.register(Category)


class TraderProfileAdmin(admin.ModelAdmin):
    list_display = ['trader', 'email_address', 'preferred_location', 'primary_category']
    search_fields = ['trader']

    class Meta:
        ordering = ['preferred_location']

admin.site.register(TraderProfile)
admin.site.register(Location)

from django.contrib import admin
from main_app.models import Listing, Category, TraderProfile, Location


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'pick_category', 'main_category']
    search_fields = ['title', 'description']

    def main_category(self, obj):
        return obj.pick_category.choose_main

admin.site.register(Listing, ListingAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['new_category', 'choose_main']
    search_fields = ['new_category', 'choose_main']

    class Meta:
        ordering = ['choose_main']

admin.site.register(Category, CategoryAdmin)


class TraderProfileAdmin(admin.ModelAdmin):
    list_display = ['trader', 'email_address', 'preferred_location', 'primary_category']
    search_fields = ['trader']

    class Meta:
        ordering = ['preferred_location']

admin.site.register(TraderProfile)
admin.site.register(Location)

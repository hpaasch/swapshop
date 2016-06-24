from django.contrib import admin
from main_app.models import Listing, Category


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'pick_category']
    search_fields = ['title', 'description']

admin.site.register(Listing, ListingAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['new_category', 'choose_main']
    search_fields = ['new_category', 'choose_main']

    class Meta:
        ordering = ['choose_main']



admin.site.register(Category, CategoryAdmin)

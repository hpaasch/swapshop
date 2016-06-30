from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views


from main_app.views import IndexView, CreateAccountView, ListingCreateView, AccountProfileView, FullListView, ListingUpdateView, ListingDeleteView, TraderProfileUpdateView, CategoryListView, CityListView, CityListingsView, SubCatListView, SubCatThumbView, SubCatGalleryView, SortNewView, SortHighView, ListDetailView
from shop_api.views import SwapShopListAPIView, SwapShopCategoryAPIView, SwapShopCategoryDetailAPIView, SwapShopSubCatAPIView, SwapShopSubCatDetailAPIView, SwapShopCatListAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^create_account/$', CreateAccountView.as_view(), name='create_account_view'),
    url(r'^listing_create/$', ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^accounts/profile/$', AccountProfileView.as_view(), name='account_profile_view'),
    url(r'^full_list/$', FullListView.as_view(), name='full_list_view'),
    url(r'^update/(?P<pk>\d+)/$', ListingUpdateView.as_view(), name='listing_update_view'),
    url(r'^delete/(?P<pk>\d+)/$', ListingDeleteView.as_view(), name='listing_delete_view'),
    url(r'^profile_update/$', TraderProfileUpdateView.as_view(), name='trader_profile_update_view'),
    url(r'^category/(?P<pk>\d+)/$', CategoryListView.as_view(), name='category_list_view'),
    url(r'^city/$', CityListView.as_view(), name='city_list_view'),
    url(r'^city_list/(?P<pk>\d+)/$', CityListingsView.as_view(), name='city_listings_view'),
    url(r'^category/(?P<subpk>\d+)/list/$', SubCatListView.as_view(), name='subcat_list_view'),
    url(r'^category/(?P<subpk>\d+)/thumb/$', SubCatThumbView.as_view(), name='subcat_thumb_view'),
    url(r'^category/(?P<subpk>\d+)/gallery/$', SubCatGalleryView.as_view(), name='subcat_gallery_view'),
    url(r'^sortnew/$', SortNewView.as_view(), name='sort_new_view'),
    url(r'^sorthigh/$', SortHighView.as_view(), name='sort_high_view'),
    url(r'^detail/(?P<pk>\d+)/$', ListDetailView.as_view(), name='list_detail_view'),

    url(r'^api/listings/$', SwapShopListAPIView.as_view(), name='swapshop_list_api_view'),
    url(r'^api/main_categories/$', SwapShopCategoryAPIView.as_view(), name='swapshop_category_api_view'),
    url(r'^api/main_categories/(?P<pk>\d+)/$', SwapShopCategoryDetailAPIView.as_view(), name='swapshop_category_detail_api_view'),
    url(r'^api/main_categories/(?P<pk>\d+)/listings/$', SwapShopCatListAPIView.as_view(), name='swapshop_catlist_api_view'),

    url(r'^api/sub_categories/$', SwapShopSubCatAPIView.as_view(), name='swapshop_subcat_api_view'),
    url(r'^api/sub_categories/(?P<pk>\d+)/$', SwapShopSubCatDetailAPIView.as_view(), name='swapshop_subcat_detail_api_view'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

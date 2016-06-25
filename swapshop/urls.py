from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.IndexView.as_view(), name='index_view'),
    url(r'^listing_create/$', views.ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^accounts/profile/$', views.AccountProfileView.as_view(), name='account_profile_view'),
    url(r'^full_list/$', views.FullListView.as_view(), name='full_list_view'),
    url(r'^update/(?P<pk>\d+)/$', views.ListingUpdateView.as_view(), name='listing_update_view'),
    url(r'^delete/(?P<pk>\d+)/$', views.ListingDeleteView.as_view(), name='listing_delete_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

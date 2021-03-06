from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm


from main_app.models import Listing, Category, Location, TraderProfile


class IndexView(ListView):
    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        return Category.objects.filter(choose_main=None)


class CreateAccountView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class ListingCreateView(CreateView):
    model = Listing
    fields = ['title', 'description', 'price', 'photo', 'city', 'pick_category']
    success_url = reverse_lazy('account_profile_view')

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.seller = self.request.user
        return super().form_valid(form)


class AccountProfileView(ListView):
    model = Listing
    template_name = 'listing_list.html'

    def get_queryset(self):
        return Listing.objects.filter(seller=self.request.user)


class TraderProfileUpdateView(UpdateView):
    fields = ['preferred_location', 'primary_category', 'email_address', 'logo']
    success_url = reverse_lazy('account_profile_view')

    def get_object(self, queryset=None):
        return self.request.user.traderprofile


class FullListView(ListView):
    model = Listing
    template_name = 'sorting/sort_low.html'

    def get_queryset(self, **kwargs):
        return Listing.objects.all().order_by('price')


class SortNewView(ListView):
    model = Listing
    template_name = 'sorting/sort_new.html'

    def get_queryset(self, **kwargs):
        return Listing.objects.all().order_by('-created')


class SortHighView(ListView):
    model = Listing
    template_name = 'sorting/sort_high.html'

    def get_queryset(self, **kwargs):
        return Listing.objects.all().order_by('-price')


class ListingUpdateView(UpdateView):
    model = Listing
    fields = ['title', 'description', 'price', 'photo', 'city', 'pick_category']
    template_name = 'listing_update.html'
    success_url = reverse_lazy('account_profile_view')


class ListingDeleteView(DeleteView):
    model = Listing
    success_url = reverse_lazy('account_profile_view')


class CategoryListView(ListView):  # this view not currently working
    model = Listing
    template_name = 'main_app/category_list.html'

    def get_queryset(self, **kwargs):
        main_cat_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(pk=main_cat_id)  # BROKEN: object_list is empty
        # return Listing.objects.filter(pick_category=main_cat_id)  # BROKEN: object_list is empty


class SubCatListView(ListView):
    model = Listing
    template_name = 'sub_cat_list.html'

    def get_queryset(self, **kwargs):
        sub_cat = self.kwargs.get('subpk', None)
        return Listing.objects.filter(pick_category=sub_cat)


class SubCatThumbView(SubCatListView):
    template_name = 'thumb.html'


class SubCatGalleryView(SubCatListView):
    template_name = 'gallery.html'


class CityListView(ListView):
    model = Location
    template_name = 'city_list_view.html'


class CityListingsView(ListView):
    model = Listing
    template_name = 'city_listings_view.html'

    def get_queryset(self, **kwargs):
        city_name = self.kwargs.get('pk', None)
        return Listing.objects.filter(city=city_name)


class ListDetailView(DetailView):
    model = Listing

    def get_queryset(self, **kwargs):
        listing_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(pk=listing_id)

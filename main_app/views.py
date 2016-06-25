from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Listing, Category


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
    template_name = 'full_list.html'


class ListingUpdateView(UpdateView):
    model = Listing
    fields = ['title', 'description', 'price', 'photo', 'city', 'pick_category']
    template_name = 'listing_update.html'
    success_url = reverse_lazy('account_profile_view')


class ListingDeleteView(DeleteView):
    model = Listing
    success_url = reverse_lazy('account_profile_view')


class CategoryListView(ListView):
    model = Listing
    template = 'category_list.html'

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(pick_category=category_id)

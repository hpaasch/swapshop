from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main_app.models import Listing

class IndexView(ListView):
    model = Listing
    template_name = 'index.html'


class ListingCreateView(CreateView):
    model = Listing
    fields = ['title', 'description', 'price', 'photo', 'location', 'pick_category']
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.seller = self.request.user
        return super().form_valid(form)


class AccountProfileView(ListView):
    model = Listing

    def get_queryset(self):
        return Listing.objects.filter(seller=self.request.user)

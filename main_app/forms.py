# so far not used

from django import forms

from main_app.models import Category, Listing

class LimitCategory(forms.ModelForm):
    class Meta:
        model = Listing

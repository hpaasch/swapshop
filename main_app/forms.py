# so far not used

from django import forms

from main_app.models import Category

class LimitCategory(forms.ModelForm):
    class Meta:
        model = Category

    def get_queryset(self):
        return Category.objects.exclude(choose_main=None)

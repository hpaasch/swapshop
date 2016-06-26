from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # very commonly used
from django.dispatch import receiver  # goes with post_save and other signals


class Location(models.Model):
    city_choice = models.CharField(max_length=20)

    def __str__(self):
        return self.city_choice


class Category(models.Model):
    new_category = models.CharField(max_length=30)
    choose_main = models.ForeignKey('self', null=True, blank=True, related_name="sub_choice")

    def __str__(self):
        return self.new_category

    class Meta:
        verbose_name_plural = "Categories"


class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='listing_photos', null=True, blank=True, verbose_name='Upload a photo')
    city = models.ForeignKey(Location)
    seller = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    pick_category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return 'http://sport.ngmnexpo.com/cliparts/2015/02/1344144.jpg'


class TraderProfile(models.Model):
    user = models.OneToOneField('auth.User')
    preferred_location = models.ForeignKey(Location, null=True, blank=True)
    primary_category = models.ForeignKey(Category, null=True, blank=True)
    email_address = models.EmailField(max_length=45, null=True, blank=True)
    logo = models.ImageField(upload_to='logo_images', null=True, blank=True, verbose_name='Upload a logo')

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return 'http://static.tumblr.com/e7snt83/tU6m7t07k/pirate_patch2.jpg'


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        TraderProfile.objects.create(user=instance)  # hooks profile to user

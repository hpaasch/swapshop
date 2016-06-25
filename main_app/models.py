from django.db import models
from django.contrib.auth.models import User

DENVER = 'Denver'
SHERRILLSFORD = 'SherrillsFord'
MOORESVILLE = 'Mooresville'
DAVIDSON = 'Davidson'
CORNELIUS = 'Cornelius'
HUNTERSVILLE = 'Huntersville'

LOCATIONS = ((DENVER, 'Denver'),
    (SHERRILLSFORD, 'SherrillsFord'),
    (MOORESVILLE, 'Mooresville'),
    (DAVIDSON, 'Davidson'),
    (CORNELIUS, 'Cornelius'),
    (HUNTERSVILLE, 'Huntersville'),
    )


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
    location = models.CharField(max_length=15, choices=LOCATIONS)
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
    trader = models.ForeignKey(User)  # could also use ('auth.User') to avoid import
    preferred_location = models.CharField(max_length=15, choices=LOCATIONS)
    primary_category = models.ForeignKey(Category, blank=True)
    contact = models.EmailField(max_length=45, blank=True)
    logo = models.ImageField(upload_to='logo_images', null=True, blank=True, verbose_name='Upload a logo')

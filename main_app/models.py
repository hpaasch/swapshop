from django.db import models
from django.contrib.auth.models import User

DENVER = 'Denver'
SHERRILLSFORD = 'SherrillsFord'
MOORESVILLE = 'Mooresville'
DAVIDSON = 'Davidson'
CORNELIUS = 'Cornelius'
HUNTERSVILLE = 'Huntersville'

WATERCRAFT = 'Watercraft'
MOTOR = 'Motor'
SAIL = 'Sail'
PADDLE = 'Paddle'
GEAR = 'Gear'
FISHING = 'Fishing'
RECREATION = 'Recreation'
SERVICES = 'Services'
LAND = 'Land'
WATER = 'Water'



class Listing(models.Model):
    LOCATIONS = ((DENVER, 'Denver'),
        (SHERRILLSFORD, 'SherrillsFord'),
        (MOORESVILLE, 'Mooresville'),
        (DAVIDSON, 'Davidson'),
        (CORNELIUS, 'Cornelius'),
        (HUNTERSVILLE, 'Huntersville'),
        )
    CATEGORIES = ((WATERCRAFT, 'Watercraft'),
        (MOTOR, 'Motor'),
        (SAIL, 'Sail'),
        (PADDLE, 'Paddle'),
        (GEAR, 'Gear'),
        (FISHING, 'Fishing'),
        (RECREATION, 'Recreation'),
        (SERVICES, 'Services'),
        (LAND, 'Land'),
        (WATER, 'Water'),
        )
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='listing_photos', null=True, blank=True, verbose_name='Upload a photo')
    location = models.CharField(max_length=15, choices=LOCATIONS)
    seller = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    # Free
    # categories

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return 'http://sport.ngmnexpo.com/cliparts/2015/02/1344144.jpg'
        # return 'https://artfiles.alphacoders.com/487/48767.jpg'
        # return '/listing_photos/default_lake_photo.jpg'

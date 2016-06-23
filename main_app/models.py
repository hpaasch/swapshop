from django.db import models
from django.contrib.auth.models import User

DENVER = 'Denver'
SHERRILLSFORD = 'SherrillsFord'
MOORESVILLE = 'Mooresville'
DAVIDSON = 'Davidson'
CORNELIUS = 'Cornelius'
HUNTERSVILLE = 'Huntersville'


class Listing(models.Model):
    CHOICES = ((DENVER, 'Denver'),
        (SHERRILLSFORD, 'SherrillsFord'),
        (MOORESVILLE, 'Mooresville'),
        (DAVIDSON, 'Davidson'),
        (CORNELIUS, 'Cornelius'),
        (HUNTERSVILLE, 'Huntersville'),
    )
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='listing_photos', null=True, blank=True, verbose_name='Upload a photo')
    location = models.CharField(max_length=15, choices=CHOICES)
    seller = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    # Free
    # categories

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return '/listing_photos/default_lake_photo.jpg'

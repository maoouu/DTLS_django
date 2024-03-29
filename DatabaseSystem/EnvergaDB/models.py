from django.db import models
from django.utils import timezone

STATUS = (
    ('Pending', 'Pending'),
    ('Acknowledged', 'Acknowledged'),
    ('Endorsed', 'Endorsed'),
    ('Recommended to President', 'Recommended to President'),
    ('Approved', 'Approved'),
    ('Denied', 'Denied'),
    ('Returned', 'Returned'),
)

CURRENT_TIME = timezone.now

# Create your models here.


class Records(models.Model):
    author = models.CharField(max_length=50, verbose_name="Author")
    description = models.CharField(max_length=100, default='No description added',
                                   verbose_name="Description")
    date_modified = models.DateField(
        auto_now=True, verbose_name="Date Modified")
    date_created = models.DateField(
        default=CURRENT_TIME, verbose_name="Date Created")
    #action_desc = models.CharField(max_length=100, verbose_name="Action Taken")
    status = models.CharField(
        max_length=100, choices=STATUS, default='Pending', verbose_name="Status")

    def __str__(self):
        return self.author

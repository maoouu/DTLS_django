from django.db import models
from django.utils import timezone

now = timezone.now()

# Create your models here.


class Records(models.Model):
    author = models.CharField(max_length=50, verbose_name="From")
    file_desc = models.CharField(max_length=100, verbose_name="File Content")
    date_created = models.DateField(default=now, verbose_name="Date Created")
    action_desc = models.CharField(max_length=100, verbose_name="Action Taken")
    status = models.CharField(max_length=100, verbose_name="Status")

    def __str__(self):
        return self.author

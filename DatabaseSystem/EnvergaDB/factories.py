from .models import Records
from django.utils import timezone

from factory.django import DjangoModelFactory


class RecordsFactory(DjangoModelFactory):
    class Meta:
        model = Records

    date_modified = timezone.now()
    date_created = timezone.now()

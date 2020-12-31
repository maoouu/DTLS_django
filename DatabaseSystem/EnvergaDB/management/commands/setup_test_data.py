import random

from django.db import transaction
from django.core.management.base import BaseCommand

from EnvergaDB.models import Records
from EnvergaDB.factories import RecordsFactory

from faker import Faker

Faker.seed(0)
fake = Faker('en_PH')
location = fake.luzon_province()
date = fake.future_date()

AUTHORS = [
    "CAS", "CED",
    "IGSR", "CCJC",
    "CBA", "CNAHS",
    "CAFA", "CME",
    "BED", "HRD",
    "OQI", "LIBRARY",
    "ICTD", "LABORATORIES"
]
FILE_DESC = [
    f"Travel To {location} On {date} [No Budget Indicated]",
    "Affiliation Fees Budget Request",
    "Info On Mass",
    "Travel Order",
    "Budget Request",
]
STATUS = [
    "Pending",
    "Acknowledged",
    "Endorsed",
    "Recommended to President",
    "Approved",
    "Denied",
    "Returned",
]
ACTIONS = [
    "Approved",
    "Forwarded",
    "Noted",
    "Viewed",
]


class Command(BaseCommand):
    help = "Generates sample data to EnvergaDB."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Records.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(20):
            RecordsFactory(
                author=random.choice(AUTHORS),
                file_desc=random.choice(FILE_DESC),
                action_desc=random.choice(ACTIONS),
                status=random.choice(STATUS)
            )
        self.stdout.write("Sample data has been generated.")

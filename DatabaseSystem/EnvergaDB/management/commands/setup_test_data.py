import random

from django.db import transaction
from django.core.management.base import BaseCommand

from EnvergaDB.models import Records
from EnvergaDB.factories import RecordsFactory

from faker import Faker

Faker.seed(0)
fake = Faker('en_PH')
DATA_COUNT = 100  # Amount of sample data to generate


class Command(BaseCommand):
    help = "Generates sample data to EnvergaDB."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Records.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(DATA_COUNT):

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

            STATUS = [
                "Pending",
                "Acknowledged",
                "Endorsed",
                "Recommended to President",
                "Approved",
                "Denied",
                "Returned",
            ]

            DESCRIPTION = [
                f"Travel To {location} On {date} [No Budget Indicated]",
                "Affiliation Fees Budget Request",
                "Info On Mass",
                "Travel Order",
                "Budget Request",
            ]

            RecordsFactory(
                author=random.choice(AUTHORS),
                description=random.choice(DESCRIPTION),
                status=random.choice(STATUS)
            )
        self.stdout.write("Sample data has been generated.")

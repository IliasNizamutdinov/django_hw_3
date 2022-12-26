import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify
from datetime import datetime
import distutils

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))


        for phone in phones:
            name = phone['name']
            price = float(phone['price'])
            image = phone['image']
            release_date = datetime.fromisoformat(phone['release_date'])
            lte_exists = bool(distutils.util.strtobool(phone['lte_exists']))
            slugs = slugify(name)
            Phone.objects.create(name = name, price = price, image = image,
                                 release_date = release_date, lte_exists = lte_exists, slug = slugs)

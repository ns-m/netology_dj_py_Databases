import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file_path = 'work_with_database\phones\phones.csv'
        with open(file_path, 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                id, name, image, price, date, lte = (line[0], line[1], line[2],
                                                     line[3], line[4], line[5])
                slug_name = name.strip().lower()
                slug_name = slug_name.replace(" ", "-")
                Phone.objects.create(id=id, name=name, image=image, price=price,
                                     release_date=date, lte_exists=lte, slug=slug_name)

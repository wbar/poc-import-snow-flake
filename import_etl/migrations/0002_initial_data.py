# -*- coding: utf-8 -*-
from django.db import models, migrations
import datetime
from dateutils import relativedelta
import os

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))


def date_dictionary(apps, schema_editor):
    DateDictionary = apps.get_model("import_etl", "DateDictionary")
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2025, 12, 31)

    while start_date <= end_date:
        dt = DateDictionary(
            src_id=start_date,
            year=start_date.year,
            month=start_date.month,
            day_of_the_month=start_date.day,
            quarter_of_the_year=int((start_date.month-1) / 3) + 1,
            half_of_the_year=int((start_date.month-1)/6) + 1
        )
        dt.save(force_insert=True)
        start_date = start_date + relativedelta(days=1)


def area_codes_dictionary(apps, schema_editor):
    AreaCodesDictionary = apps.get_model('import_etl', 'AreaCodesDictionary')
    with open(os.path.join(fixture_dir, 'postcodes_list'), 'r') as fh:
        for line in fh.readlines():
            try:
                a = AreaCodesDictionary(src_id=line.strip())
                a.save()
            except:
                print(line)
                raise


def property_types(apps, schema_editor):
    """
    Choices class for Property types based on:
    https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd
    """
    PropertyTypesDictionary = apps.get_model('import_etl', 'PropertyTypesDictionary')
    for item in ('Detached', 'Semi-Detached', 'Terraced', 'Flats'):
        p = PropertyTypesDictionary(src_id=item[0], name=item)
        p.save()


def new_property_types(apps, schema_editor):
    """
    Relates to New and Old property
    """
    NewPropertyTypesDictionary = apps.get_model('import_etl', 'NewPropertyTypesDictionary')
    for item in ('Y = a newly built property', 'N = an established residential building'):
        p = NewPropertyTypesDictionary(src_id=item[0], name=item)
        p.save()


def duration_types(apps, schema_edit):
    """
    Relates to the tenure: F = Freehold, L-Leasehold etc.
    """
    DurationTypesDictionary = apps.get_model('import_etl', 'DurationTypesDictionary')
    for item in ('Freehold', 'Leasehold'):
        p = DurationTypesDictionary(src_id=item[0], name=item)
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('import_etl', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(date_dictionary),
        migrations.RunPython(area_codes_dictionary),
        migrations.RunPython(property_types),
        migrations.RunPython(new_property_types),
        migrations.RunPython(duration_types),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCodesDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('src_id', models.CharField(unique=True, max_length=4)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Area Code',
                'verbose_name_plural': 'Area Codes',
            },
        ),
        migrations.CreateModel(
            name='DateDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('src_id', models.DateField(verbose_name='Date')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('month', models.PositiveSmallIntegerField(verbose_name='Month')),
                ('day_of_the_month', models.PositiveSmallIntegerField(verbose_name='Day of the month')),
                ('quarter_of_the_year', models.PositiveSmallIntegerField(verbose_name='Quarter of the month')),
                ('half_of_the_year', models.PositiveSmallIntegerField(verbose_name='Half of the year')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DurationTypesDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('src_id', models.CharField(unique=True, max_length=1)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Duration type',
                'verbose_name_plural': 'Duration types',
            },
        ),
        migrations.CreateModel(
            name='NewPropertyTypesDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('src_id', models.CharField(unique=True, max_length=1)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'New property type',
                'verbose_name_plural': 'New property types',
            },
        ),
        migrations.CreateModel(
            name='PropertyTypesDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('src_id', models.CharField(unique=True, max_length=1)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Property type',
                'verbose_name_plural': 'Property types',
            },
        ),
        migrations.CreateModel(
            name='SaleFacts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('transaction_uid', models.UUIDField(unique=True, db_index=True, verbose_name='Transaction unique identifier', help_text='A reference number which is generated automatically recording each published sale. The number is unique and will change each time a sale is recorded.')),
                ('price', models.PositiveIntegerField(help_text='Sale price stated on the transfer deed.')),
                ('area_code', models.ForeignKey(to='import_etl.AreaCodesDictionary')),
                ('date_of_transfer', models.ForeignKey(to='import_etl.DateDictionary', help_text='Date when the sale was completed, as stated on the transfer deed.')),
                ('duration', models.ForeignKey(to='import_etl.DurationTypesDictionary')),
                ('new_property', models.ForeignKey(to='import_etl.NewPropertyTypesDictionary')),
                ('property_type', models.ForeignKey(to='import_etl.PropertyTypesDictionary')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Sale fact',
                'verbose_name_plural': 'Sale facts',
            },
        ),
    ]

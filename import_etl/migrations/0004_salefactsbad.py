# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_etl', '0003_nulls'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleFactsBad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('row', models.TextField()),
                ('exc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

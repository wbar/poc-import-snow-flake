from django.db import models, migrations


def generate_zeros(apps, schema_editor):
    """
    Method generates NULL interpretation
    """
    DurationTypesDictionary = apps.get_model('import_etl', 'DurationTypesDictionary')
    NewPropertyTypesDictionary = apps.get_model('import_etl', 'NewPropertyTypesDictionary')
    PropertyTypesDictionary = apps.get_model('import_etl', 'PropertyTypesDictionary')
    for item in (DurationTypesDictionary, NewPropertyTypesDictionary, PropertyTypesDictionary):
        item(pk=0, src_id='', name='NULL').save(force_insert=True)


class Migration(migrations.Migration):

    dependencies = [
        ('import_etl', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(generate_zeros),
    ]

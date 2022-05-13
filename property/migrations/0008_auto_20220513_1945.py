# Generated by Django 2.2.24 on 2022-05-13 16:45
import phonenumbers

from django.db import migrations


def get_correct_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = phonenumbers.parse(
            flat.owners_phonenumber,
            'RU'
        )
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(get_correct_number)
    ]
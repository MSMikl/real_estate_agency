# Generated by Django 2.2.24 on 2022-05-16 13:09

from django.db import migrations


def set_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.iterator(chunk_size=200):
        for owner in Owner.objects.filter(name=flat.owner1).iterator():
            owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220516_1619'),
    ]

    operations = [
        migrations.RunPython(set_flats_to_owners)
    ]

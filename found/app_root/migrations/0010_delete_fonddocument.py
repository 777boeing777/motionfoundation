# Generated by Django 4.1.3 on 2022-11-30 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_remove_fonddocument_files_fonddocument_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FondDocument',
        ),
    ]
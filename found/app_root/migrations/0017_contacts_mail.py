# Generated by Django 4.1.6 on 2023-03-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0016_alter_gallery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='mail',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]

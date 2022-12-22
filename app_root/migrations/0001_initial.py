# Generated by Django 4.1.3 on 2022-11-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_field', models.FileField(blank=True, upload_to='files_storage/', verbose_name='file')),
                ('is_fond_doc', models.BooleanField(db_index=True, help_text='is file corporate or not', verbose_name='is fond doc')),
            ],
        ),
        migrations.CreateModel(
            name='FondDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capture', models.CharField(blank=True, max_length=256, verbose_name='capture')),
                ('files', models.ManyToManyField(related_name='fond_docs', to='root.file')),
            ],
        ),
    ]

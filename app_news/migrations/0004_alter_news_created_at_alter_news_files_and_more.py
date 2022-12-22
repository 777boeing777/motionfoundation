# Generated by Django 4.1.3 on 2022-11-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0011_alter_answer_question_alter_contacts_address'),
        ('news', '0003_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and time of public news.'),
        ),
        migrations.AlterField(
            model_name='news',
            name='files',
            field=models.ManyToManyField(related_name='news', to='root.file', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last update'),
        ),
    ]

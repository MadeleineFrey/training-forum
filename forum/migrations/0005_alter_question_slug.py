# Generated by Django 3.2 on 2022-02-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20220215_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]

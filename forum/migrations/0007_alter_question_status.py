# Generated by Django 3.2 on 2022-02-16 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_remove_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]

# Generated by Django 3.2 on 2022-02-15 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_question_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]

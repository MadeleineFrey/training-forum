# Generated by Django 3.2 on 2022-02-16 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_question_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answered',
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_record_primary_contact_tel_record_budget_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='emms',
        ),
        migrations.RemoveField(
            model_name='record',
            name='fp',
        ),
        migrations.RemoveField(
            model_name='record',
            name='hiv',
        ),
        migrations.RemoveField(
            model_name='record',
            name='malaria',
        ),
        migrations.RemoveField(
            model_name='record',
            name='mnch',
        ),
    ]
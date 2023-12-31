# Generated by Django 3.2.12 on 2023-08-18 23:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US', unique=True),
        ),
    ]

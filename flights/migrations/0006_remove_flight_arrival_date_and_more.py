# Generated by Django 4.2.1 on 2023-05-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_airline_alter_flight_airline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_date',
        ),
    ]
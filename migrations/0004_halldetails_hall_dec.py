# Generated by Django 4.0 on 2023-04-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheEventJoyApp', '0003_alter_booking_booked_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='halldetails',
            name='hall_dec',
            field=models.CharField(default=' ', max_length=10000),
        ),
    ]

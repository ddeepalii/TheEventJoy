# Generated by Django 4.0 on 2023-04-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheEventJoyApp', '0006_rename_date_booking_hall_date_alter_booking_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

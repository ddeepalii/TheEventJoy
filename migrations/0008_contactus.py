# Generated by Django 4.0 on 2023-05-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheEventJoyApp', '0007_alter_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=' ')),
                ('query', models.CharField(max_length=1000)),
            ],
        ),
    ]

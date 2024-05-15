from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
import datetime


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session,on_delete=models.CASCADE)


class HallSlot(models.Model):
    timeslot = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.timeslot}'


class HallDetails(models.Model):
    hallname = models.CharField(max_length=200, primary_key=True)
    guests = models.IntegerField(default=" ")
    halltype = models.CharField(max_length=200)
    hall_dec = models.CharField(max_length=10000, default=" ")
    # halltime = models.ForeignKey(HallSlot, on_delete=models.CASCADE, default=" ", null=True)
    hall_image = models.ImageField(null=True, blank=True, upload_to='TheEventJoy/Images', default="")

    def __str__(self):
        return f'{self.hallname}'


class CategoryFood(models.Model):
    cname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cname}'


class DetailFood(models.Model):
    fid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    fprice = models.IntegerField(default=" ")
    fcategory = models.ForeignKey(CategoryFood, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return f'{self.fid} : {self.fname}'


class Booking(models.Model):
    user = models.CharField(max_length=100)
    timeslot = models.CharField(max_length=100)
    hall_date = models.DateField()
    bill = models.CharField(max_length=500)
    booked_hall = models.CharField(max_length=200)
    items_json = models.CharField(max_length=10000, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} has booked {self.booked_hall} for {self.hall_date} for timeslot {self.timeslot}. Booking Done at {self.timestamp}'


class Contactus(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=" ")
    query = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.id}: {self.user}'

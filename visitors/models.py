from django.db import models
from django.contrib.auth.models import User
from staff.models import Hotel,Image
import datetime
from django.urls import reverse





class RoomType(models.Model):
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.room_type} Rate:{self.price} "





class Room(models.Model):

    DIRECTION_VIEWS_CHOICES =[
        ('Svn', 'Sea view North'),
        ('Svs', 'Sea view South'),
        ('Gvn', 'Garden view North'),
        ('Gvs', 'Garden view South'),
    ]

    room_nbr = models.IntegerField(null=False)
    floor = models.IntegerField(null=False)
    room_view_direction =  models.CharField(max_length=30, choices=DIRECTION_VIEWS_CHOICES)
    nbr_peoples= models.IntegerField(null=False)
    nbr_beds = models.IntegerField(null=False)
    room_size = models.ForeignKey(RoomType, on_delete=models.CASCADE, default = None)
    images = models.ManyToManyField(Image)

    def __repr__(self):
        return f"Room Number {self.room_nbr} FL {self.floor} Type {self.room_size}"


    def __str__(self):
        return f"Room Number {self.room_nbr} FL {self.floor} Type {self.room_size}"




class Customer(models.Model):
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"




class Booking(models.Model):
    arrival = models.DateField(auto_now=False) 
    departure = models.DateField(auto_now=False)
    room = models.ForeignKey(Room, on_delete = models.CASCADE) 
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    nbr_ppl = models.IntegerField()

    def __str__(self):
        return f"{self.customer}Booked Room {self.room}from {self.arrival}{self.departure}"

    def get_absolute_url(self):
        return reverse('booking_detail', args=[str(self.id)])
# this is to get back the booking after we did it here id has better usage thatn PK -django 



class GuestsMessage(models.Model):
    guest = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

def __str__(self):
        return f"{self.guest}{self.guest.room.room_nbr}"





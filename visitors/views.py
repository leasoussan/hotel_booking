from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import * 
import datetime
from django.db.models import Q



def home(request):
    if request.method == "GET":
        form = SearchBookingForm()
        return render(request, 'visitors/homepage.html', {"form":form})


def check_availability_form(request):
    print("function activated")
    if request.method == "POST":
        print(request.POST)
        
        available_rooms = Room.objects.filter(nbr_peoples__gte = request.POST['nbr_peoples']
        ).exclude(
            booking__arrival__gte = request.POST['arrival'],  booking__departure__lte = request.POST['arrival']
        ).exclude(
            booking__arrival__lte = request.POST['departure'], booking__departure__gte = request.POST['departure'])
        print(available_rooms)
        request.session['arrival']= request.POST['arrival']
        request.session['departure']= request.POST['departure']
        request.session['nbr_peoples']= request.POST['nbr_peoples']
        return render(request, 'visitors/available_rooms.html', {"available_rooms":available_rooms})
    


def book_room(request, pk):
    room = Room.objects.get(id=pk)
    
    booking = Booking.objects.create(
        room = room, 
        arrival = request.session['arrival'], 
        departure= request.session['departure'], 
        nbr_ppl = request.session['nbr_peoples'],
        customer = request.user.customer
        )
    
    return redirect('my_booking', booking.id)


class MyBookings(generic.ListView):
    model = Booking
    template_name = 'my_booking.html'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        return context




class RoomView(generic.DetailView):
    
    model = Room
    template_name = 'visitors/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Fetch a room
        # context['Title'] = f"Room {self.room_type}" #add a heading
        return context



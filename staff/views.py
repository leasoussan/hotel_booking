from django.shortcuts import render
from django.views import generic
# from django.views.generic import ListView, DetailView
from visitors.models import *


class BookingsView(generic.ListView):
    model = Booking
    template_name = 'staff/booking.html'



class BookingDetail(generic.DetailView):
    model = Booking 
    template_name = 'booking/book_room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headng']= "Booking Details"
        return context

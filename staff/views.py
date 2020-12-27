from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from visitors.models import Booking
from django.urls import reverse_lazy

class BookingsView(ListView):
    model = Booking
    template_name = 'staff/bookings.html'



class BookingDetail(DetailView):
    model = Booking 
    template_name = 'staff/booking_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading']= "Booking Details"
        return context


class CreateBooking(CreateView):
    model= Booking
    template_name = 'staff/create_booking.html'
    fields = '__all__'



class UpdateBooking(UpdateView):
    model = Booking
    template_name = 'staff/edit_booking.html'
    fields = ['arrival', 'departure', 'room', 'nbr_ppl']


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'staff/delete_booking.html'
    success_url = reverse_lazy('bookings_home')
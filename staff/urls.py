from django.urls import path, include
from . import views

urlpatterns = [       
    path('booking/', views.BookingsView.as_view(), name = "bookings_home"),
    path('booking/<int:pk>', views.BookingDetail.as_view(), name = "booking_detail"),
]
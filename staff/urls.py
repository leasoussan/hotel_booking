from django.urls import path, include
from . import views
from.views import BookingsView, BookingDetail, CreateBooking, UpdateBooking, DeleteBooking

urlpatterns = [       
    path('booking/', views.BookingsView.as_view(), name = "bookings_home"),
    path('booking/<int:pk>', views.BookingDetail.as_view(), name = "booking_detail"),
    path('new_booking', views.CreateBooking.as_view(), name = "new_booking"),
    path('edit_booking/<int:pk>', views.UpdateBooking.as_view(), name = "edit_booking"),
    path('delete_booking/<int:pk>', views.DeleteBooking.as_view(), name = "delete_booking"),

]
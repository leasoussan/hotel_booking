from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('search/', views.check_availability_form, name = "search"),
    path('book_room/<int:pk>', views.book_room, name = "book_room"),
    path('room/<int:pk>', views.RoomView.as_view(), name = "detail_room"),
    path('my_booking/<int:pk>', views.MyBookings.as_view(), name = "my_booking"),    
]
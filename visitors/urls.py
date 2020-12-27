from django.urls import path
from . import views 
from .views import AboutView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name = "home"),
    path('about/', AboutView.as_view(), name = "about"),
    path('search/', views.check_availability_form, name = "search"),
    path('book_room/<int:pk>', views.book_room, name = "book_room"),
    path('room/<int:pk>', views.RoomView.as_view(), name = "detail_room"),
    path('my_booking/<int:pk>', views.MyBookings.as_view(), name = "my_booking"),    
]
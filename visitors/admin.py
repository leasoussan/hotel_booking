from django.contrib import admin
from visitors.models import * 


admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Booking)
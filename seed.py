
import django 
import os
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torquay.settings')
django.setup()
from visitors.models import *
from staff.models import *
from django.contrib.auth.models import User
from visitors.models import Customer, Room
from django_seed import Seed

seeder = Seed.seeder()


room_types = ['BR_1_Single', 'BR_1_Double', 'BR_2_Single', 'BR_2_Double', 'PH_1br', 'PH_2br' ]




def pop_room_type(type_list, price_start=100):

    for r_type in type_list:
        room_type = RoomType(room_type = r_type, price = price_start)   
        room_type.save()
        price_start += 50
        # here we change the value of the room start price after we save that the next one will be +50 from thepreviouse one
    


roomfloor= 5
floors = 10

def pop_room(floors = floors, room_per_floor = roomfloor):
    for floor_num in range(1, floors+1):

        for room_num  in range(1, room_per_floor+1):
            floor = floor_num
            room_view_direction =  random.choice(
                [('Svn', 'Sea view North'),
                ('Svs', 'Sea view South'),
                ('Gvn', 'Garden view North'),
                ('Gvs', 'Garden view South'),
            ])[0]
            nbr_peoples= random.choice(range(1,6))
            nbr_beds = nbr_peoples / 2
            room_size = random.choice(RoomType.objects.all())

            
                # if floor < floors-1:
                #     room_size = random.choice(RoomType.objects.exclude('PH_1br', 'PH_2br'))
                # else: 
                #     room_size = random.choice(RoomType.objects.get('PH_1br', 'PH_2br'))


            room = Room(room_nbr = room_num,
            floor = floor,
            room_view_direction = room_view_direction,
            nbr_peoples= nbr_peoples,
            nbr_beds = nbr_beds,
            room_size = room_size)

            room.save()
            print(f'Created Room :{room.id}')


# pop_room_type(room_types)
pop_room()
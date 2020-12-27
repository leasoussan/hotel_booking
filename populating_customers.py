
import django
# os to interact with computer 
import os
from faker import Faker
import random
# setting the env 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torquay.settings')
# this line will check for the setting to know where to save it 
django.setup()
# after the above step >> we can import models 
from visitors.models import Customer
from django.contrib.auth.models import User



fake_c = Faker()

def pop_users(n):
    for i in range(n):
        user = User.objects.create_user(
            first_name = fake_c.first_name(),
            last_name =fake_c.last_name(),
            email = fake_c.email(),
            username =  fake_c.user_name())
        user.save()
        
        customer = Customer.objects.create(
            phone_number=fake_c.phone_number(),
            address=fake_c.address(),
            city=fake_c.city(),
            country =fake_c.country(),     
            user = user,       
            )
    
        customer.save()
        print(f'Created Customer:{customer.id}')
    
    # finished
    print(f"Finished...{n} entries populated.")


# pop_users(30)


                # 
        

def pop_booking(n):
    # for i in range(n):
    # booking = Booking(
    #     arrival= 
    #     departure = 
    #     room = 
    #     customer
    #     nbr_ppl = 
    #     )
    pass


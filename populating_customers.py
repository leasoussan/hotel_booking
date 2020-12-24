
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


def populating_customers(n):
    for i in range(n):
        # generating fake data
        f_first_name = fake_c.first_name()
        f_last_name = fake_c.last_name()
        f_email = fake_c.email()
        
        
        # creating data object and saving to DB
        customer = Customer(
            phone_number=fake_c.phone_number(),
            address=fake_c.address(),
            city=fake_c.city(),
            country =fake_c.country(),
            user = User.objects.create_user(username=f_first_name, password = f_last_name)
        )
        customer.save()
        print(f'Created Customer:{customer.id}')
    
    # finished
    print(f"Finished...{n} entries populated.")



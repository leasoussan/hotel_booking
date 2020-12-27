from django.contrib.auth.models import AbstractUser

from django.db import models


# this is another way to do the registration and the usage for the customer-user model
# let's say we want the regula form but we want to add a fileds -age
# class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(null = True, blank =True)
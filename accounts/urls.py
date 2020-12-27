from django.urls import path, include
from .views import Register, SignUpView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('signup/', SignUpView.as_view(), name='signup'),
]


from django import forms
from django.forms import ModelForm
from .models import Booking
from bootstrap_datepicker_plus import DatePickerInput

# because we are not looking into a model this is not  modelForm
class SearchBookingForm(forms.Form):
    arrival = forms.DateTimeField()
    departure = forms.DateTimeField()
    nbr_peoples = forms.IntegerField()




class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }
    
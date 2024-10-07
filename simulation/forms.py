# simulation/forms.py

from django import forms

class SimulationForm(forms.Form):
    chassis_number = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=10)
    seatbelt_worn = forms.BooleanField(required=False)

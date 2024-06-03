from django import forms
from .models import Feeding, Toy

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name']
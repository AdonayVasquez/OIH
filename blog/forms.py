from django import forms
from .models import Aspirantes

class ContactForm(forms.ModelForm):
    class Meta:
        model = Aspirantes
        fields = '__all__'
"""
    Author: Peter Murimi
"""
from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=20)
    contact_email = forms.EmailField()
    content = forms.CharField(max_length=200)
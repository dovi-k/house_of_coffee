"""
Contact Form in About Page
"""
from django import forms


class ContactForm(forms.Form):
    """
    Contact Form fields for Contact Form in About App
    """
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

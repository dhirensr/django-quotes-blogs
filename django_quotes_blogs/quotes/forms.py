from django import forms
from django.forms import Textarea
from .models import Quotes

class QuotesForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ["quotes_text"]
        labels = {'quotes_text': "Quote"}
        widgets = {
            'quotes_text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

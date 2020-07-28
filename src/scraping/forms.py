from django import forms
from scraping.models import City, Language

class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), required=False,
        widget=forms.Select(attrs={'class' : 'form-control'}),
        label='Город'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), required=False,
        widget=forms.Select(attrs={'class' : 'form-control'}),
        label='Специальность'
    )

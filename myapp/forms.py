from django import forms
from .models import exersice, setgroup


class CreateSetGroupForm(forms.ModelForm):
    exersice = forms.ModelChoiceField(
        queryset=exersice.objects.all(),
        widget=forms.Select,
        label="Select exercise",
    )
    
    class Meta:
        model: setgroup
        fields = ['workout', 'exersice', 'order', 'notes']
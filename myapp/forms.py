from django import forms
from .models import setgroup, set


class CreateSetGroupForm(forms.ModelForm):
    class Meta:
        model = setgroup
        fields = [ 'exercise', 'notes']
        

class CreateSetForm(forms.ModelForm):
    class Meta:
        model = set
        fields = ['weight', 'reps']
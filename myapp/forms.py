from django import forms
from .models import setgroup


class CreateSetGroupForm(forms.ModelForm):
    
    class Meta:
        model = setgroup
        fields = [ 'exercise', 'notes']
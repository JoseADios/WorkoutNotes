from django import forms
from .models import setgroup, set


class CreateSetGroupForm(forms.ModelForm):
    class Meta:
        model = setgroup
        fields = [ 'exercise', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notes'].required = False


class CreateSetForm(forms.ModelForm):
    class Meta:
        model = set
        fields = ['weight', 'reps']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
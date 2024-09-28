from django import forms
from .models import setgroup, set, exercise


class CreateSetGroupForm(forms.Form):
    # obtener todos los ejercicios menos el que esta relacionado con el workout

    exercise = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        workout_id = kwargs.pop('workout_id')
        super(CreateSetGroupForm, self).__init__(*args, **kwargs)
        
        existing_exercises = setgroup.objects.filter(workout_id=workout_id).values_list('exercise_id', flat=True)
        available_exercises = exercise.objects.exclude(id__in=existing_exercises)
        
        self.fields['exercise'].choices = available_exercises.values_list('id', 'name')


class CreateSetForm(forms.ModelForm):
    class Meta:
        model = set
        fields = ['weight', 'reps']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = exercise
        fields = ['name', 'description', 'type', 'muscle']
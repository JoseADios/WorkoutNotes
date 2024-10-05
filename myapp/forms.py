from django import forms
from .models import setgroup, set, exercise, workout, muscle


class CreateSetGroupForm(forms.Form):
    # obtener todos los ejercicios menos el que esta relacionado con el workout

    exercise = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        workout_id = kwargs.pop('workout_id')
        muscle = kwargs.pop('muscle')
        super(CreateSetGroupForm, self).__init__(*args, **kwargs)
        
        existing_exercises = setgroup.objects.filter(workout_id=workout_id, exercise__muscle=muscle).values_list('exercise_id', flat=True)
        available_exercises = exercise.objects.filter(muscle=muscle).exclude(id__in=existing_exercises)
        
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
    muscle = forms.ModelMultipleChoiceField(queryset=muscle.objects.all(), required=True, widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        muscle_id = kwargs.pop('muscle_id')
        super().__init__(*args, **kwargs)
        self.fields['muscle'].initial = [muscle.objects.get(id=muscle_id)]

    class Meta:
        model = exercise
        fields = ['name', 'description', 'type']
        

class UpdateWorkoutForm(forms.Form):
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    notes = forms.CharField(max_length=200, required=False)
    

    def __init__(self, *args, **kwargs):
        workout_id = kwargs.pop('workout_id')
        super(UpdateWorkoutForm, self).__init__(*args, **kwargs)
        self.fields['created_at'].initial = workout.objects.get(id=workout_id).created_at
        self.fields['notes'].initial = workout.objects.get(id=workout_id).notes
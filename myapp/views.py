from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import workout, setgroup, set
from django.db.models.functions import Cast
from django.db.models import DateField
from datetime import datetime
from .forms import CreateSetGroupForm, CreateSetForm

# Create your views here.

WORKOUT = 1

def hello(request):
    return render(request, 'index.html')


def workouts(request):
    workouts = workout.objects.all()
    return render(request, 'workouts/workouts.html', {
        'workouts': workouts})


def workout_detail(request, id):
    if request.method == 'POST':
        set.objects.create(
            setgroup_id=request.POST['setgroup_id'], reps=request.POST['reps'], weight=request.POST['weight']
        )
        return redirect('workout_detail', id)

    elif request.method == 'GET':
        workout_object = workout.objects.get(id=id)
        order = setgroup.objects.filter(workout=workout_object).count() + 1

        return render(request, 'workouts/detail.html', {
            'workout': workout_object,
            'order': order,
            'set_form': CreateSetForm()
            })


def create_workout(request):
    if request.method == 'GET':
        # si no hay workout para ese dia crea uno
        today = datetime.now()

        todayWork = workout.objects.annotate(date__only=Cast(
            'created_at', DateField())).filter(date__only=today)

        if len(todayWork) > 0:
            todayWork = todayWork[0]

        if not todayWork:
            todayWork = workout.objects.create(user=request.user)

        order = setgroup.objects.filter(workout=todayWork).count() + 1

        return render(request, 'workouts/detail.html', {
            'workout': todayWork,
            'order': order
        })

    elif request.method == 'POST':
        return render(request, 'workouts/create_workout.html', {})


def create_setgroup(request, workout_id, order):
    if request.method == 'GET':
        return render(request, 'setgroups/create.html', {
            'form': CreateSetGroupForm()
        })

    elif request.method == 'POST':
        setgroup.objects.create(
            workout_id=workout_id, exercise_id=request.POST['exercise'], notes=request.POST['notes'], order=order)
        
        return redirect('workout_detail', workout_id)


def delete_setgroup(request, pk):
    workout_id = get_object_or_404(setgroup, id=pk).workout.id
    setgroup.objects.get(id=pk).delete()
    return redirect('workout_detail', workout_id)


def delete_set(request, pk, workout_id):
    set.objects.get(id=pk).delete()
    return redirect('workout_detail', workout_id)

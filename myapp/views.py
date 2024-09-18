from django.shortcuts import render
from myapp.models import workout, setgroup
# from django.utils import timezone
from django.db.models.functions import Cast
from django.db.models import DateField
from datetime import datetime
from .forms import CreateSetGroupForm

# Create your views here.


def hello(request):
    return render(request, 'index.html')


def workouts(request):
    workouts = workout.objects.all()
    return render(request, 'workouts/workouts.html', {
        'workouts': workouts})


def workout_detail(request, id):
    workout_object = workout.objects.get(id=id)
    order = setgroup.objects.filter(workout=workout_object).count() + 1

    return render(request, 'workouts/detail.html', {
        'workout': workout_object,
        'order': order})


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
        print(request.POST)
        setgroup.objects.create(
            workout_id=workout_id, exercise_id=request.POST['exercise'], notes=request.POST['notes'], order=order)


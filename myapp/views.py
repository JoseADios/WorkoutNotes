from django.shortcuts import render
from myapp.models import workout
from django.utils import timezone
from django.db.models.functions import Cast
from django.db.models import DateField


# Create your views here.


def hello(request):
    return render(request, 'index.html')


def workouts(request):
    workouts = workout.objects.all()
    return render(request, 'workouts/workouts.html', {
        'workouts': workouts})


def workout_detail(request, id):
    workout_object = workout.objects.get(id=id)
    return render(request, 'workouts/detail.html', {
        'workout': workout_object})


def create_workout(request):
    if request.method == 'GET':
        # si no hay workout para ese dia crea uno
        today = timezone.now().date()

        todayWork = workout.objects.annotate(date__only=Cast('date', DateField())).filter(date__only=today)
        
        if not todayWork:
            print('no hay workout para ese dia')
            workout.objects.create(user=request.user)
        
        
        return render(request, 'workouts/create_workout.html', {
            'wdate': todayWork
        })
    else:
        return render(request, 'workouts/create_workout.html', {})
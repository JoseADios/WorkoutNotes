from django.shortcuts import render
from myapp.models import workout

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
        
        return render(request, 'workouts/create_workout.html', {})
    else:
        return render(request, 'workouts/create_workout.html', {})
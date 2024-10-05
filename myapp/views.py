from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from myapp.models import workout, setgroup, set, exercise, muscle
from django.db.models.functions import Cast
from django.db.models import DateField
from datetime import datetime
from .forms import CreateSetGroupForm, CreateSetForm, CreateExerciseForm, UpdateWorkoutForm
from .utils import reorder_setgroup_after_delete
from django.db import IntegrityError
# Create your views here.

REST_TIME = 120


def index(request):
    are_training = False

    todayWork = workout.objects.filter(created_at__date=timezone.localdate())

    if len(todayWork) > 0:
        are_training=True
    
    return render(request, 'index.html', {
        'are_training': are_training
    })


def workouts(request):
    workouts = workout.objects.all().order_by('-created_at')
    return render(request, 'workouts/workouts.html', {
        'workouts': workouts})


def workout_detail(request, id):
    if request.method == 'POST':
        if 'save_set' in request.POST:
            set.objects.create(
                setgroup_id=request.POST['setgroup_id'], reps=request.POST['reps'], weight=request.POST['weight']
            )
        elif 'update_set' in request.POST:
            set_obj = get_object_or_404(set, id=request.POST['set_id'])
            set_obj.reps = request.POST['reps']
            set_obj.weight = request.POST['weight']

            set_obj.save()

        return redirect('workout_detail', id)

    elif request.method == 'GET':
        workout_object = workout.objects.get(id=id)
        edit_work = False

        if 'edit' in request.GET:
            edit_work = True

        return render(request, 'workouts/detail.html', {
            'workout': workout_object,
            'set_form': CreateSetForm(),
            'edit_work': edit_work,
            'workout_form': UpdateWorkoutForm(workout_id=workout_object.id),
            'rest_time': REST_TIME
        })


def create_workout(request):
    if request.method == 'GET':
        
        # si no hay workout para ese dia crea uno
        todayWork = workout.objects.filter(created_at__date=timezone.localdate())

        if len(todayWork) > 0:
            todayWork = todayWork[0]

        if not todayWork:
            todayWork = workout.objects.create(user=request.user)

        return redirect('workout_detail', todayWork.id)

    elif request.method == 'POST':
        return render(request, 'workouts/create_workout.html', {})


def workout_update(request, workout_id):
    workout_obj = get_object_or_404(workout, id=workout_id)

    if request.method == 'POST':
        
        # si se cambia la fecha 
        # si existe un workout en esa fecha 
        # mover los setgroups a ese workout
        # eliminar el actual
        new_date = datetime.fromisoformat(request.POST.get('created_at')).date()
        
        if workout_obj.created_at != request.POST.get('created_at'):
            existent_workout = workout.objects.filter(created_at__date=new_date)
            
            if existent_workout and existent_workout[0].id != workout_id:
                existent_workout = existent_workout[0]
                
                setgroup.objects.filter(workout_id=workout_obj.id).update(workout=existent_workout)
                    
                workout_obj.delete()
            
                return redirect('workout_detail', existent_workout.id)
            
            else:
                workout_obj.created_at = request.POST.get('created_at')
                workout_obj.notes = request.POST.get('notes')
                workout_obj.save()
                
                return redirect('workout_detail', id=workout_id)


def select_muscle(request, workout_id):
    return render(request, 'setgroups/muscles.html', {
        'workout_id': workout_id,
        'muscles': muscle.objects.all()
    })

def create_setgroup(request, workout_id, muscle_id):
    error = ''
    form = CreateSetGroupForm(request.POST or None, workout_id=workout_id, muscle=muscle_id)


    if request.method == 'GET':
        return render(request, 'setgroups/create.html', {
            'form': form,
            'workout_id': workout_id,
            'muscle_id': muscle_id
        })

    elif request.method == 'POST':
        order = setgroup.objects.filter(workout_id=workout_id).count() + 1

        try:
            setgroup.objects.bulk_create(
                [
                    setgroup(workout_id=workout_id,
                             exercise_id=exercise_id, order=(order+i))
                    for i, exercise_id in enumerate(request.POST.getlist('exercise'), start=0)
                ]
            )
            return redirect('workout_detail', workout_id)

        except IntegrityError:
            error = f'Error, el ejercicio ya existe: {
                request.POST.getlist("exercise")}'

        return render(request, 'setgroups/create.html', {
            'form': form,
            'error': error,
            'workout_id': workout_id,
            'muscle_id': muscle_id
        })


def delete_setgroup(request, pk):
    workout_id = get_object_or_404(setgroup, id=pk).workout.id
    setgroup.objects.get(id=pk).delete()
    reorder_setgroup_after_delete(workout_id=workout_id)
    return redirect('workout_detail', workout_id)


def delete_set(request, pk, workout_id):
    set.objects.get(id=pk).delete()
    return redirect('workout_detail', workout_id)


def create_exercise(request, workout_id, muscle_id):
    if request.method == 'POST':

        post = request.POST
        exercise_obj = exercise.objects.create(
            name=post['name'], description=post['description'], type=post['type'])
        exercise_obj.muscle.set(post.getlist('muscle'))

        return redirect('create_setgroup', workout_id, muscle_id)
    elif request.method == 'GET':
        return render(request, 'exercises/create.html', {
            'form': CreateExerciseForm(muscle_id=muscle_id),
            'muscle_id': muscle_id,
            'workout_id': workout_id
        })

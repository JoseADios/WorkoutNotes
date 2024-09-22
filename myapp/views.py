from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import workout, setgroup, set
from django.db.models.functions import Cast
from django.db.models import DateField
from datetime import datetime
from .forms import CreateSetGroupForm, CreateSetForm
from .utils import reorder_setgroup_after_delete

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
        if 'save_set' in request.POST:
            set.objects.create(
                setgroup_id=request.POST['setgroup_id'], reps=request.POST['reps'], weight=request.POST['weight']
            )
        elif 'update_set' in request.POST:
            print(request.POST)
            set_obj = get_object_or_404(set, id=request.POST['set_id'])
            set_obj.reps = request.POST['reps']
            set_obj.weight = request.POST['weight']

            set_obj.save()

        return redirect('workout_detail', id)

    elif request.method == 'GET':
        workout_object = workout.objects.get(id=id)

        return render(request, 'workouts/detail.html', {
            'workout': workout_object,
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

        return redirect('workout_detail', todayWork.id)

    elif request.method == 'POST':
        return render(request, 'workouts/create_workout.html', {})


def create_setgroup(request, workout_id):
    error = ''

    if request.method == 'GET':
        return render(request, 'setgroups/create.html', {
            'form': CreateSetGroupForm(),
            'workout_id': workout_id,
        })

    elif request.method == 'POST':
        order = setgroup.objects.filter(workout_id=workout_id).count() + 1
        form = CreateSetGroupForm(request.POST)

        try:
            setgroup_instance = form.save(commit=False)
            setgroup_instance.workout_id = workout_id
            setgroup_instance.order = order
            setgroup_instance.save()

            return redirect('workout_detail', workout_id)
        except:
            error = f'Error, el ejercicio ya existe: {form.errors}'

        return render(request, 'setgroups/create.html', {
            'form': form,
            'error': error,
            'workout_id': workout_id,
        })


def delete_setgroup(request, pk):
    workout_id = get_object_or_404(setgroup, id=pk).workout.id
    setgroup.objects.get(id=pk).delete()
    reorder_setgroup_after_delete(workout_id=workout_id)
    return redirect('workout_detail', workout_id)


def delete_set(request, pk, workout_id):
    set.objects.get(id=pk).delete()
    return redirect('workout_detail', workout_id)

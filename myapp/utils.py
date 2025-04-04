from .models import setgroup, set

""" 
Cuando se elimina un elemento


cuando se reordena recibir:

    id, order
    2,  1
    1,  3
    3,  2
"""

# funcion para ordenar despues de eliminar

def reorder_setgroup_after_delete(workout_id):
    setgroups = setgroup.objects.filter(workout_id=workout_id).order_by('order')

    for i in range(len(setgroups)):
        if setgroups[i].order != i + 1:
            setgroups[i].order = i + 1
    
    setgroups.bulk_update(setgroups, ['order'])
    
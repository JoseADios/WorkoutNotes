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
    print(setgroups)
    for i in range(len(setgroups)):
        print('Iteracion ', i+1)
        if setgroups[i].order != i + 1:
            print('No tiene el orden correcto ', setgroups[i].order)
            setgroups[i].order = i + 1
    
    # update
    setgroups.bulk_update(setgroups, ['order'])
    
    print('ordered list ', setgroups)
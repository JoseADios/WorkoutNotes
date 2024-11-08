from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workouts', views.workouts, name='workouts'),
    path('workouts/<int:id>', views.workout_detail, name='workout_detail'),
    path('workouts/create', views.create_workout, name='create_workout'),
    path('workouts/<int:workout_id>/update', views.workout_update, name='workout_update'),
    path('workouts/<int:pk>/delete', views.workout_delete, name='workout_delete'),
    path('setgroup/<int:workout_id>/<int:muscle_id>/create', views.create_setgroup, name='create_setgroup'),
    path('setgroup/<int:workout_id>/select_muscle', views.select_muscle, name='select_muscle'),
    path('setgroup/<int:pk>/delete/', views.delete_setgroup, name='setgroup_delete'),   
    path('set/<int:workout_id>/<int:pk>/delete/', views.delete_set, name='set_delete'),   
    path('exercises/<int:workout_id>/<int:muscle_id>/create/', views.create_exercise, name='create_exercise'),
    path('sign_in', views.sign_in, name='sign_in'),
]

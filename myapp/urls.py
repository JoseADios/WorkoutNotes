from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('workouts', views.workouts, name='workouts'),
    path('workouts/<int:id>', views.workout_detail, name='workout_detail'),
    path('workouts/create', views.create_workout, name='create_workout'),
    path('workouts/<int:workout_id>/update', views.workout_update, name='workout_update'),
    path('setgroup/<int:workout_id>/create', views.create_setgroup, name='create_setgroup'),
    path('setgroup/<int:pk>/delete/', views.delete_setgroup, name='setgroup_delete'),   
    path('set/<int:workout_id>/<int:pk>/delete/', views.delete_set, name='set_delete'),   
    path('exercises/create/<int:workout_id>', views.create_exercise, name='create_exercise')
]

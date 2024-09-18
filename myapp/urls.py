from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('workouts', views.workouts, name='workouts'),
    path('workouts/<int:id>', views.workout_detail, name='workout_detail'),
    path('create_workout', views.create_workout, name='create_workout'),
    path('create_setgroup <int:workout_id> <int:order>', views.create_setgroup, name='create_setgroup'),
    
]

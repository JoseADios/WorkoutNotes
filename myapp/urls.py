from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('workouts', views.workouts, name='workouts'),
    path('workouts/<int:id>', views.workout_detail, name='workout_detail'),
    path('workouts/create', views.create_workout, name='create_workout'),
    path('setgroup/<int:workout_id>/<int:order>/create', views.create_setgroup, name='create_setgroup'),
    path('setgroup/<int:pk>/delete/', views.delete_setgroup, name='setgroup_delete'),   
]

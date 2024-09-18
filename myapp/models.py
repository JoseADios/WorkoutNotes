from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.date.strftime('%d-%m-%Y %H:%M:%S')
           

class muscle(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class excersice(models.Model):
    
    WEIGHT_REPS = 'W_R'
    DISTANCE_TIME = 'D_T'
    WEIGHT_DISTANCE = 'W_D'
    WEIGHT_TIME = 'W_T'
    REPS_DISTANCE = 'R_D'
    REPS_TIME = 'R_T'
    WEIGHT = 'W'
    REPS = 'R'
    DISTANCE = 'D'
    TIME = 'T'
    
    EXCERSICE_TYPE_CHOICES = (
        (WEIGHT_REPS, 'Weight and Reps'),
        (DISTANCE_TIME, 'Distance and Time'),
        (WEIGHT_DISTANCE, 'Weight and Distance'),
        (WEIGHT_TIME, 'Weight and Time'),
        (REPS_DISTANCE, 'Reps and Distance'),
        (REPS_TIME, 'Reps and Time'),
        (WEIGHT, 'Weight'),
        (REPS, 'Reps'),
        (DISTANCE, 'Distance'),
        (TIME, 'Time'),
    )
    
    muscle = models.ManyToManyField('muscle')
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=3, choices=EXCERSICE_TYPE_CHOICES, default=WEIGHT_REPS)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class superset(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class set(models.Model):
    setgroup = models.ForeignKey('setgroup', on_delete=models.CASCADE, blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    rir = models.IntegerField(default=1)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.setgroup.excersice.name} - {self.reps} x {self.weight} kg'

class setgroup(models.Model):
    workout = models.ForeignKey('workout', on_delete=models.CASCADE)
    excersice = models.ForeignKey('excersice', on_delete=models.DO_NOTHING)
    superset = models.ForeignKey('superset', on_delete=models.DO_NOTHING, blank=True, null=True)
    order = models.IntegerField(default=1)
    notes = models.TextField(max_length=200, blank=True, null=True)

    
    class Meta:
        unique_together = ('workout', 'order')
        
    def __str__(self):
        return self.excersice.name
    
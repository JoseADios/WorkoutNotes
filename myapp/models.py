from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
           


class muscle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    

class excersice(models.Model):
    muscle = models.ManyToManyField('muscle')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class set(models.Model):
    workout = models.ForeignKey(workout, on_delete=models.CASCADE)
    excersice = models.ForeignKey('excersice', on_delete=models.DO_NOTHING)
    biserie = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='biserie_set' ,blank=True, null=True)
    triserie = models.ForeignKey('self', on_delete=models.DO_NOTHING, related_name='triserie_set', blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.excersice.name + ' ' + str(self.reps)
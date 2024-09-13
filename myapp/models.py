from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    

class superset(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class set(models.Model):
    set_group = models.ForeignKey('set_group', on_delete=models.CASCADE, blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    notes = models.TextField(max_length=200, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.excersice.name + ' ' + str(self.reps)

class set_group(models.Model):
    workout = models.ForeignKey('workout', on_delete=models.CASCADE)
    excersice = models.ForeignKey('excersice', on_delete=models.DO_NOTHING)
    superset = models.ForeignKey('superset', on_delete=models.DO_NOTHING, blank=True, null=True)
    order = models.IntegerField(default=1)
    notes = models.TextField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            try:
                last_order = set_group.objects.filter(set_group=self.set_group).latest('order').order
                self.order = last_order + 1
            except set_group.DoesNotExist:
                self.order = 1
        super().save(*args, **kwargs)
    
    def clean(self):
        if set_group.objects.filter(set_group=self.set_group, order=self.order).exists():
            raise ValidationError('El orden ya existe en este set group')
    
    class Meta:
        unique_together = ('workout', 'order')
        
    def __str__(self):
        return self.excersice.name
    
from django.contrib import admin
from .models import excersice, workout, muscle, set, setgroup, superset

# Register your models here.
admin.site.register(excersice)
admin.site.register(workout)
admin.site.register(muscle)
admin.site.register(set)
admin.site.register(setgroup)
admin.site.register(superset)
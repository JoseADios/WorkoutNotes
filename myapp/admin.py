from django.contrib import admin
from .models import exersice, workout, muscle, set, setgroup, superset

# Register your models here.
admin.site.register(exersice)
admin.site.register(workout)
admin.site.register(muscle)
admin.site.register(set)
admin.site.register(setgroup)
admin.site.register(superset)
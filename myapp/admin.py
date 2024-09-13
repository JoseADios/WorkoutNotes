from django.contrib import admin
from .models import excersice, workout, muscle, set

# Register your models here.
admin.site.register(excersice)
admin.site.register(workout)
admin.site.register(muscle)
admin.site.register(set)
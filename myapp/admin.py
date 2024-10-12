from django.contrib import admin
from .models import exercise, workout, muscle, set, setgroup, superset, UserProfile

# Register your models here.
admin.site.register(exercise)
admin.site.register(workout)
admin.site.register(muscle)
admin.site.register(set)
admin.site.register(setgroup)
admin.site.register(superset)
admin.site.register(UserProfile)
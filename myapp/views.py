from django.shortcuts import render
from myapp.models import setgroup

# Create your views here.

def hello(request):
    return render(request, 'index.html')

def workouts(request):
    setgroups = setgroup.objects.all()
    return render(request, 'workouts.html', {
        'setgroups': setgroups})
from django.shortcuts import render
from .models import Student

# Create your views here.

#function based views are declared here - khan

def index(request):
    return render(request,'students/index.html', {

        'students' : Student.objects.all()

    })


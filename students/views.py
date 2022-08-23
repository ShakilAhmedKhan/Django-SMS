from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student

# Create your views here.

#function based views are declared here - khan

def index(request):
    return render(request,'students/index.html', {

        'students' : Student.objects.all()

    })

def view_student(request, id):
    student = Student.object.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

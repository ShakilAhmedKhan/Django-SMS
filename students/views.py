from django.shortcuts import render

# Create your views here.

#function based views are declared here - khan

def index(request):
    return render(request,'students/index.html')


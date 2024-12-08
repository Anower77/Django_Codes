from django.shortcuts import render
from .forms import Form
from . import models
# from .models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')


# forms
def form(request):
    form = Form()
    return render(request, 'forms.html', {'form':form})

# models 
def student_list_view(request):
    students = models.Student.objects.all()
    return render(request, 'student_list.html',  {'students': students})
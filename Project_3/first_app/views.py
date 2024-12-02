from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    dic = {'author': 'Rahim', 'age' : 4, 'lst' : [2, 3, 4], 'value': " ", 'animal': "cat\ndog\nhorse", 'birthday' : datetime.datetime.now(),'course' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : '3000'
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : '5000'
        },
        {
            'id' : 3,
            'name' : 'C++',
            'fee' : '7000'
        },
    ]}
    return render(request, 'home.html', dic)
    
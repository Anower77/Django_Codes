from django.http import HttpResponse


def home(request):
    return HttpResponse("This is Home Pageee...???")

def contact(request):
    return HttpResponse("This is New Contact Pages..??")


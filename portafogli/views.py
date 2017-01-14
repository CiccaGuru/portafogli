from django.http import HttpResponse
import datetime

def homepage(request):
    return HttpResponse("Benvenuto in portafogli!")

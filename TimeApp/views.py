from django.shortcuts import render, HttpResponse
import datetime, time
# Create your views here.
def index(request):
    date_time = {
        'date' : datetime.datetime.now().strftime('%Y-%m-%d'),
        'time' : time.strftime('%H:%M:%S', time.localtime()),
    }
    return render(request, 'index.html' , date_time)

def style(request):
    date_time = {
        'date' : datetime.datetime.now().strftime('%Y-%m-%d'),
        'time' : time.strftime('%H:%M:%S', time.localtime()),
    }
    return render(request, 'time_date.html' , date_time)

def js(request):
    return render(request, 'time_js.html')
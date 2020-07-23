from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import sys

# Create your views here.
DEBUG = (sys.argv[1] == 'runserver')

def home(request):
    return render(request, 'home.html', {'name':'Select the date-time to check if it matches with your system date-time'})

def check(request):
    url_date=request.GET['date1']
    now = datetime.now()
    res=HttpResponse()
    dt_string = now.strftime("%Y-%m-%dT%H:%M")
    if url_date==dt_string:
        return HttpResponse("selected date: "+url_date+"<br>current date: "+dt_string+"<h1>STATUS CODE : "+str(res.status_code)+"</h1><br><h2><i>*Current date of your system and the date you chose are <b>MATCHING</b></i></h2>")
    else:
        return HttpResponse("selected date: "+url_date+"<br>current date: "+dt_string+"<h1>STATUS CODE : "+str(res.status_code)+"</h1><br><h2><i>*Current date of your system and the date you chose are <b>NOT</b> matching</i></h2>")

def servercheck(request):
    if DEBUG==True:
        return HttpResponse('{"status":"OK"}')
    
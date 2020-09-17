from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
  return HttpResponse('Hi, current server time is {now}'.format(
    now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
  ))

def home_routes(request):
  return render(request, 'routes.html')
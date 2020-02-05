from django.http import HttpResponse
import json
import User
from models import User
from models import TestResult
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def redirect_to_login(request):
    return redirect('/login/')

def results (request):
    all_results = TestResult.objects.all().filter(user=User.get_username())
    return render(request, 'resuts.html', {'all_results' : all_results})
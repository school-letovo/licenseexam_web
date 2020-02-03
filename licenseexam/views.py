from django.http import HttpResponse
import json
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


def redirect_to_login(request):
    return redirect('/login/')

from django.http import HttpResponse
import json
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index_page(request):
    return render(request, "index.html", {})

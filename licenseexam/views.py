from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from licenseexam.models import TestResult
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


def index(request):
    return render(request, "index.html", {"title": "Page"})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_new_result(request):
    res = TestResult()
    try:
        res.datetime_completed = datetime.time()
        res.question_count = int(request.POST["question_count"])
        res.result_time = int(request.POST["result_time"])
        res.user = request.user
    except Exception as e:
        return HttpResponse("Error adding data to database: " + str(e))
    res.save()
    print("Added result for user " + str(request.user) + ': ' + str(request.POST))
    return HttpResponse("OK")


def results(request):
    all_results = TestResult.objects.all().filter(user=request.user)
    return render(request, 'results.html', {'all_results' : all_results, "title": "Results", "user": request.user})
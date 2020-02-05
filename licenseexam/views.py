from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from licenseexam.models import TestResult


def redirect_to_login(request):
    return redirect('/login/')

@csrf_exempt
def add_new_result(request):
    if not request.user.is_authenticated:
        return HttpResponse("Error: User is not authenticated")
    if request.method != "POST":
        return HttpResponse("Error: Request method is not POST")
    res = TestResult()
    res.datetime_completed = datetime.time()
    res.question_count = int(request.POST.data["question_count"])
    res.result_time = request.POST.data["result_time"]
    res.user = request.user
    res.save()
    print("Added result for user " + str(request.user))
    return HttpResponse("OK")


def results(request):
    all_results = TestResult.objects.all().filter(user=request.user)
    return render(request, 'results.html', {'all_results' : all_results})


from django.http import HttpResponse
import json
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.view.generic.edit import FromView
from django.contrib.auth import UserCreatinForm
from django.views.decorators.csrf import csrf_exempt


def index_page(request):
    return render(request, "index.html", {})

def login_page(request):
    return render(request, "login.html", {})

class RegisterFromView (FromView):
    form_class = UserCreatinForm
    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFromView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFromView, self).form_invalid(form)

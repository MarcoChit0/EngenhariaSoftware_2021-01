from django.http import HttpResponse, Http404
from django.shortcuts import render

# Esse é o controller

from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Welcome to Academy System")

def show_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        raise Http404("User does not exists")
    return HttpResponse(f"Welcome, user {user.name}, Your id is: {user.pk} and you password {user.password}")

def test(request):
    return render(request, "academyManage/test.html")

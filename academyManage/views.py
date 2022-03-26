from django.http import HttpResponse, Http404
from django.shortcuts import render

# Esse é o controller

from .models import User, Client
# Create your views here.

def index(request):
    return HttpResponse("Welcome to Academy System")

def cadastrar(request):
    pass

def show_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        raise Http404("User does not exists.")
    return HttpResponse(f"Welcome, user {user.name}, Your id is: {user.pk} and you password {user.password}")


# UC 14
def make_payment(request, user_id):
    pass

# UC 10
def make_membership(request, user_id):
    pass

# UC 16
def hire_service(request, user_id):
    assert User(user_id).user_type == 'cliente'
    assert Client(user_id).membership_status == 'active'
    pass

def test(request):
    return render(request, "academyManage/test.html")

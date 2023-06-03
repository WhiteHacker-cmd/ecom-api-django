from django.shortcuts import render
from rest_framework.authtoken import views #this if for later use 
from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({"info": "online shopping", "products": "5000000000000000000"})
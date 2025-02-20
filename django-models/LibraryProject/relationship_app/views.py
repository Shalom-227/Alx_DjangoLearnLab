from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def relationship_app_view(Request):
    return HttpResponse("This is the relationship_app view")


from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

data = {

    "Name: Woneata Stallworth ",
    "Track: Backend(Python) ",
    "Message: Hi, mentor. Fingercrossed I don't have to redo this lol ",
    

}

def index(request):
    return HttpResponse(data)

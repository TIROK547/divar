from django.shortcuts import render
from django.http.response import HttpResponse

ITEMS = []

def add_item(request,name):
    global ITEMS
    ITEMS.append(name)
    return HttpResponse("item added")

def get_items(request):
    return HttpResponse(ITEMS)

def home(request):
    return render(request,"./templates/interaction/main.html")
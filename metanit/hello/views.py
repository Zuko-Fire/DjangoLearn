from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render


def index(request):
    num = int(request.GET.get("num"))
    data = {"n": num}
    return render(request, "index.html", context=data)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
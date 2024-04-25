from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def function (request):
    # return render(request,"index.html")
    return HttpResponse("server start")
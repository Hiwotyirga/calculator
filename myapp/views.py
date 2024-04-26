from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def function (request):
    return render(request,"index.html")

def submitquery1(request):
    print(request.GET)  # Check the contents of GET parameters in the console
    try:
        q = request.GET["query"]
        return HttpResponse(q)
    except KeyError:
        return HttpResponse("Query parameter is missing", status=400)



    
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def function (request):
    return render(request,"index.html")

def submitquery1(request):
    q = request.GET["query"]
    try:
        ans=eval(q)
        dictionary={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render (request, "index.html",context=dictionary)
    except Exception as e:
        dictionary={
            "error-message":str(e),
            "error":True,
            "result":False
        }
        return render (request,"index.html",context=dictionary)
        
     

    



    
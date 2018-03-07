from django.shortcuts import render
from django.http.response import HttpResponse

def index(request, name='World'):
    # return HttpResponse("<h1>Hello " + name + "</h1>")
    return render(request, "hello.html", {
        "name": name,
    })

def contact(request):
    return render(request, "contact.html")

from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from django.http import Http404
import json
import os

# Create your views here.
def cv(request, username='lejenome'):
    print(__file__)
    basedir = os.path.dirname(__file__)
    cv_path = os.path.join(basedir, "users", username + ".json")
    # if not os.path.isfile(cv_path):
    #     raise Http404("cv not found")
    # with open(cv_path) as f:
    #     data = json.load(f)
    try:
        with open(cv_path) as f:
            data = json.load(f)
    except:
         raise Http404("cv not found")
    return render(request, "cv.html", data)

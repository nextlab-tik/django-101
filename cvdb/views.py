from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseNotFound
from django.http import Http404
import json
import os
from .models import CV, Experience, Education

# Create your views here.
def cv(request, username='lejenome'):
    cv = get_object_or_404(CV, username=username)
    experience = cv.experience_set.all()
    education = cv.education_set.all()
    return render(request, "cvdb.html", {
        "cv": cv,
        "experience": experience,
        "education": education,
        "skills": {
            "proficiency": cv.skills_proficiency.all(),
            "familiar": cv.skills_familiar.all(),
        }
    })

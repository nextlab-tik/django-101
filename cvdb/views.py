from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseNotFound
from django.http import Http404
import json
import os
from .models import Person, Experience, Education

# Create your views here.
def cv(request, username='lejenome'):
    person = get_object_or_404(Person, username=username)
    experience = person.experience_set.all()
    education = person.education_set.all()
    return render(request, "cvdb.html", {
        "person": person,
        "experience": experience,
        "education": education,
        "skills": {
            "proficiency": person.skills_proficiency.all(),
            "familiar": person.skills_familiar.all(),
        }
    })

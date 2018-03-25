from django.contrib import admin
from .models import Person, Experience, Education, Skill

# Register your models here.
admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)

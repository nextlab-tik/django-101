from django.contrib import admin
from .models import CV, Experience, Education, Skill

# Register your models here.
admin.site.register(CV)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)

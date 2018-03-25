from django.contrib import admin
from .models import Task

# Register your models here.
# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'is_done')
    list_display = ('__str__', 'id', 'title', 'is_done')

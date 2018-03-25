from django.shortcuts import render, redirect
from .models import Task

#tasks = [
#    {"id": 0, "title": "Hit the gym", "done": False},
#    {"id": 1, "title": "Pay bills", "done": True},
#    {"id": 2, "title": "Meet George", "done": False},
#]
# Create your views here.
def index(request):
    # TODO
    tasks = Task.objects.all()
    return render(request, "todo.html", {
        "tasks": tasks,
    })

def delete(request, task_id):
    # TODO
    #global tasks
    #tasks = [task for task in tasks if task['id'] != int(task_id)]
    # Task.objects.get(pk=task_id).delete()
    # TODO alternative ???
    Task.objects.filter(pk=task_id).delete()
    return redirect("tasks-list")

def add(request):
    # TODO
    #tasks.append({
    #    "id": len(tasks),
    #    "title": request.POST['title'],
    #    "done": False,
    #})
    # SOL 1
    #from datetime import datetime
    #Task.objects.create(
    #    title=request.POST['title'],
    #    created_at=datetime.now(),
    #)
    # SOL 2
    t = Task()
    t.title = request.POST['title']
    # t.created_at = datetime.now()
    t.save()
    return redirect("tasks-list")

def toggle(request, task_id):
    # TODO
    #for task in tasks:
    #    if task['id'] == int(task_id):
    #        task['done'] = not task['done']
    t = Task.objects.get(pk=task_id)
    t.is_done = not t.is_done
    t.save()
    # TODO alternative ???
    return redirect("tasks-list")

from django.shortcuts import render, redirect

tasks = [
    {"id": 0, "title": "Hit the gym", "done": False},
    {"id": 1, "title": "Pay bills", "done": True},
    {"id": 2, "title": "Meet George", "done": False},
]
# Create your views here.
def index(request):
    return render(request, "todo.html", {
        "tasks": tasks,
    })

def delete(request, task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != int(task_id)]
    return redirect("tasks-list")

def add(request):
    tasks.append({
        "id": len(tasks),
        "title": request.POST['title'],
        "done": False,
    })
    return redirect("tasks-list")

def toggle(request, task_id):
    for task in tasks:
        if task['id'] == int(task_id):
            task['done'] = not task['done']
    return redirect("tasks-list")

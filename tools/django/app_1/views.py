from django.shortcuts import render, redirect
from .models import Users, Task
from .forms import CreatNewTask


# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def show_users(request):
    """ show the users insede model or table User """
    names = Users.objects.all()
    return render(request, 'user_page.html', {
        'names': names
        
    })
def show_task(request):
    """ from model or class or table we going ti filter by id the tittle """
    tasks = Task.objects.all()
    return render(request, 'task_page.html', {
        'tasks': tasks
        
    })

def new_task(request):
    if request.method == "GET":
        return render(request,'new_task.html',{
            'form': CreatNewTask()
        })
    else:
        Task.objects.create(title=request.POST["title"], description=request.POST["description"], project_id = 6)
        return redirect("/")

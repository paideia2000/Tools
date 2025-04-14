from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users, Task
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def show_users(request, id):
    """ show the users insede model or table User """
    get_name = get_object_or_404(Users, id=id)
    return render(request, 'user_page.html', {
        'name': get_name.email
        
    })

def show_task(resquest, id):
    """ from model or class or table we going ti filter by id the tittle """
    get_task = get_object_or_404(Task, id=id)
    return HttpResponse('Need learn: ' + get_task.description)
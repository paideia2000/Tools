from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users, Task
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def page_1(request):
    out_put1 = HttpResponse('<h1 style="color: blueviolet; font-size: 50px">HOLA MUNDO</h1>')
    return out_put1

def show_users(request):
    """ show the users insede model or table User """
    project = get_list_or_404(Users.objects.values())
    return JsonResponse(project, safe=False)


def show_task(resquest, id):
    """ from model or class or table we going ti filter by id the tittle """
    get_task = get_object_or_404(Task, id=id)
    return HttpResponse('Need learn:' + get_task.description)
from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home_page),
    path("user/", v.show_users),
    path("task/", v.show_task),
    path("new_task/", v.new_task),
    path("saved", v.saved)
]
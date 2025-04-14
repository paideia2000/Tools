from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home_page),
    path("user/<int:id>", v.show_users),
    path("task/<int:id>", v.show_task),
]
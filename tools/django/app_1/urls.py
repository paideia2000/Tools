from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.page_1),
    path("u/", v.show_users),
    path("t/<int:id>", v.show_task),
]
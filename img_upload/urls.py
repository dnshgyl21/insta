from django.urls import path
from .import views


urlpatterns=[
    path("",views.upload),
    path("display",views.display),
    path("delete",views.delete),
    path("edit_text",views.editText),
]
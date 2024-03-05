from django.urls import path

from lea import views

urlpatterns = [
    path("", views.index, name="index"),
]
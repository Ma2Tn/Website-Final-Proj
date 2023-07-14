from django.urls import path
from appstore import views

urlpatterns = [
    path("", views.home, name="appstore"),
]
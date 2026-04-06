from django.urls import path
from funney.views import home
urlpatterns = [
    path("home/",home)
]
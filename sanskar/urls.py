from django.urls import path
from sanskar import views
urlpatterns=[
    path("",views.home),
    path("home/",views.home,name="home_page"),
    path("contact/",views.contact ,name="contact_page" ),
    path("projects/",views.projects,name="projects_page"),
    path("projects/<id>/",views.projects,name="projects_page"),
]
from django.urls import path
from .views import home, contact, projects, resume

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("projects/", projects, name="projects"),
    path("resume/", resume, name="resume"),
]

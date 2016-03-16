from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project

class CourseList(ListView):
    model = Project

class CourseDetail(DetailView):
    model = Project

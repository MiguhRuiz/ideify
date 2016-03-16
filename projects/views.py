from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project

class ProjectList(ListView):
    model = Project

class ProjectDetail(DetailView):
    model = Project

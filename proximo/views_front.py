from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = "Project/Project_list.html"
    model = Project
    context_object_name = "Project"


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "Project/Project_detail.html"
    model = Project


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Project/Project_update.html"
    model = Project
    fields = "__all__"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "Project/Project_create.html"
    model = Project
    fields = "__all__" # "__all__" for all of them


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Project/Project_delete.html"
    model = Project
    success_url = reverse_lazy("Project_list")

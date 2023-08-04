from django.urls import path
from .views_front import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="Project_list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="Project_detail"),
    path("create/", ProjectCreateView.as_view(), name="Project_create"),
    path("<int:pk>/update/", ProjectUpdateView.as_view(), name="Project_update"),
    path("<int:pk>/delete/", ProjectDeleteView.as_view(), name="Project_delete"),
]

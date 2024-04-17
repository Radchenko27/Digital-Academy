from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('project/new/', views.project_create, name="project_create"),
    path('project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project')
]

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task
from django.views import View
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from django.shortcuts import render

# -----------------------FBV-Function  Based Views---------------------------------
# --------------------index-----------------------------------------------

# Первый вариант
# def index(request):
#     projects_list_url = reverse('tasks:project_list')
#     html = f"<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>Список проектов</a>"
#     return HttpResponse(html)

# Второй вариант
# def index(request):
#     template = render_to_string('tasks/index.html')
#     return HttpResponse(template)

def index(request):
    return render(request, "tasks/index.html")


# ------------------------------------------------------------------------

# def another_page(request):
#     return HttpResponse("Это другая страница приложения tasks.")

# ----------------------project_list---------------------------------

# Первый вариант
# def project_list(request):
#     projects = Project.objects.all()
#     projects_html = '<h1> Список проектов </h1> <ul>'
#     for project in projects:
#         projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#     projects_html += "</ul>"
#     return HttpResponse(projects_html)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

# ----------------------project_detail---------------------------------

# Первый вариант
# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     tasks = project.tasks.all()
#     response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
#     response_html += '<h2>Задачи</h2><ul>'
#     for task in tasks:
#         response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#     response_html += f'</ul>'
#     return HttpResponse(response_html)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})


# -----------------------task_detail---------------------------------

# Первый вариант
# def task_detail(request, project_id, task_id):
#     project = get_object_or_404(Project, id=project_id)
#     task = get_object_or_404(Task, id=task_id, project=project)
#     response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#     return HttpResponse(response_html)

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})


# -----------------------CBV-Class Based Views---------------------------------

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'tasks/index.html')
# class ProjectListView(ListView):
#     model = Project
#     template_name = "tasks/projects_list.html"
#
# class ProjectDetailList(DetailView):
#     model = Project
#     pk_url_kwarg = 'project_id'
#     template_name = 'tasks/project_detail.html'
#
# class TaskDetailView(DetailView):
#     model = Task
#     pk_url_kwarg = 'task_id'
#     template_name = 'tasks/task_detail.html'


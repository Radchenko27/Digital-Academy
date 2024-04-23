from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView


# Create your views here.

# ------------------------Function Based Views---------------------------------------------------------------------------------------------------------------
def index_1(request):
    bugs_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качества </h1><p><a href='{bugs_list_url}'> Список всех багов</a><p>"
            f"<p><a href='{feature_list_url}'>Запрос на улучшение</a><p>")
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1> Список отчётов об ошибках </h1><ul>'
    for bug in bugs:
        bugs_html += f"<li><a href='{bug.id}/'> {bug.title}</a>     {bug.status}</li>"
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1> Список отчётов об ошибках </h1><ul>'
    for feature in features:
        features_html += f"<li><a href='{feature.id}/'> {feature.title}</a>    {feature.status}</li>"
    features_html += "</ul>"
    return HttpResponse(features_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    html = (f'<h1>{bug.title}</h1>'
            f'<p><i>Описание: </i> {bug.description}</p>'
            f'<p><i>Статус: </i> {bug.status}</p>'
            f'<p><i>Приоритет: </i> {bug.priority}</p>'
            f'<p><i>Проект: </i> {bug.project}</p>'
            f'<p><i>Задание: </i> {bug.task}</p>')
    return HttpResponse(html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    html = (f'<h1>{feature.title}</h1>'
            f'<p><i>Описание: </i> {feature.description}</p>'
            f'<p><i>Статус: </i> {feature.status}</p>'
            f'<p><i>Приоритет: </i> {feature.priority}</p>'
            f'<p><i>Проект: </i> {feature.project}</p>'
            f'<p><i>Задание: </i> {feature.task}</p>')
    return HttpResponse(html)


# ------------------------Class Based Views---------------------------------------------------------------------------------------------------------------

# class Index_1_View(View):
#     def get(self, request, *args, **kwargs):
#         bugs_list_url = reverse('quality_control:bug_list')
#         feature_list_url = reverse('quality_control:feature_list')
#         html = (f"<h1>Система контроля качества </h1><p><a href='{bugs_list_url}'> Список всех багов</a><p>"
#                 f"<p><a href='{feature_list_url}'>Запрос на улучшение</a><p>")
#         return HttpResponse(html)

# class BugReportDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#
#     def get(self, request, *args, **kwargs):
#         bug = self.get_object()
#         html = (f'<h1>{bug.title}</h1>'
#             f'<p><i>Описание: </i> {bug.description}</p>'
#             f'<p><i>Статус: </i> {bug.status}</p>'
#             f'<p><i>Приоритет: </i> {bug.priority}</p>'
#             f'<p><i>Проект: </i> {bug.project}</p>'
#             f'<p><i>Задание: </i> {bug.task}</p>')
#         return HttpResponse(html)


# class FeatureRequestView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#
#     def get(self, *args, **kwargs):
#         feature = self.get_object()
#         html = (f'<h1>{feature.title}</h1>'
#                 f'<p><i>Описание: </i> {feature.description}</p>'
#                 f'<p><i>Статус: </i> {feature.status}</p>'
#                 f'<p><i>Приоритет: </i> {feature.priority}</p>'
#                 f'<p><i>Проект: </i> {feature.project}</p>'
#                 f'<p><i>Задание: </i> {feature.task}</p>')
#         return HttpResponse(html)

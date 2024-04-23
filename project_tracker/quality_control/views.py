from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404


# Create your views here.

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
        bugs_html += f"<li><a href='{bug.id}/'> {bug.title}</a></li>"
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1> Список отчётов об ошибках </h1><ul>'
    for feature in features:
        features_html += f"<li><a href='{feature.id}/'> {feature.title}</a></li>"
    features_html += "</ul>"
    return HttpResponse(features_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    html = f'Детали бага <{bug_id}>'
    return HttpResponse(html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    html = f'Детали улучшения <{feature_id}>'
    return HttpResponse(html)

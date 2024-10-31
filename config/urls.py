from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from config.views import (
    RandomNumberTemplateView,
    hello_world, 
    hello_world_json,
    RandomNumberView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('json/', hello_world_json),
    path("todo/", include("todo.urls")),
    path("api/todo/", include("todo.api_urls")),
    path("random/template/", RandomNumberTemplateView.as_view()),
    path("random/view/", RandomNumberView.as_view()),
] 

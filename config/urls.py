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
    path("todo/", include("todo.urls")),
    # 127.0.0.1:8000/api-auth/login/
    # 127.0.0.1:8000/api-auth/logout/ -> session flush
    path("api-auth/", include("rest_framework.urls")),
    path("api/blog/", include("blog.api_urls")),
    path("api/product/", include("product.api_urls")),
    path("api/brand/", include("brand.api_urls")),
    path("api/todo/", include("todo.api_urls")),
    path("random/template/", RandomNumberTemplateView.as_view()),
    path("random/view/", RandomNumberView.as_view()),
] 

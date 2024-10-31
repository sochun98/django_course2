from django.urls import path
from todo.views import TodoCreateView, todo_list, todo_detail, todo_detail_name


# 127.0.0.1:8000/todo/
urlpatterns = [
    # VIEWS
    path("create/", TodoCreateView.as_view()),
    path("list/", todo_list),
    path("<int:pk>/", todo_detail),
    path("<str:name>/", todo_detail_name),
]
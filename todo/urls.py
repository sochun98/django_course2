from django.urls import path
from todo.views import TodoCreateView, TodoDetailView, TodoListView, TodoUpdateView, todo_detail, todo_detail_name


# 127.0.0.1:8000/todo/
urlpatterns = [
    # VIEWS
    path("create/", TodoCreateView.as_view()),
    path("list/", TodoListView.as_view()),
    path("<int:pk>/", TodoDetailView.as_view()),
    path("update/<int:pk>/", TodoUpdateView.as_view()),
    path("<str:name>/", todo_detail_name),
]
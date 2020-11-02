from django.urls import path
from app.views import TodoListAndCreate, TodoDetailChangeAndCreate

urlpatterns = [
    path('',TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndCreate.as_view())
]
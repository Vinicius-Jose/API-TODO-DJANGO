from rest_framework.decorators import api_view
from app.models import Todo
from app.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
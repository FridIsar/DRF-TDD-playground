from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo, Animal
from todos.permissions import UserIsOwnerTodo
from todos.serializers import TodoSerializer, AnimalSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerTodo)

class AnimalCreateAPIView(ListCreateAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    permission_classes = (IsAuthenticated)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

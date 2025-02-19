from django.urls import path
from todos.views import TodoListCreateAPIView, TodoDetailAPIView, AnimalCreateAPIView

app_name = 'todos'

urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),
    path('animal/', AnimalCreateAPIView.as_view(), name="animal"),
]

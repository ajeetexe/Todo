from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TodoModel
from .serializers import TodoSerializer

class TodoList(ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset  = TodoModel.objects.all()
    serializer_class = TodoSerializer

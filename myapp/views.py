from django.shortcuts import render

from rest_framework import generics
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
# Create your views here.

#pasar variables  desde la vista, HTLM y logica.
def home(request):
    productos = [
        {"nombre": "Camisa", "precio": 20},
        {"nombre": "Pantalón", "precio": 35},
    ]
    return render(request, "miapp/home.html", {
        "nombre": "Carlos",
        "productos": productos
    })

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#step 3 create request REST: create, get, update, delete
#with base to model in ths case fo users

#class for obtain list and for create users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
#class with that allows update, delete users for by ID 
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
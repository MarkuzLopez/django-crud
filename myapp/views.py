from django.shortcuts import render, redirect

from rest_framework import generics
from .models import Task, User, Product

#IMPORT FORMS
from .forms import ProductForm

from .serializers import TaskSerializer, UserSerializer
#step 3 for create form with template
#view of forms, with template DTL.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # redirige a otra vista después de guardar
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()    
    # filter conditional
    # __lt: menor que || __lte: menor o igual || __gt: mayor que || __gte: mayor o igual || __icontains: contiene texto (sin distinguir mayúsculas)    
    # productFilt = Product.objects.filter(name='Laptop')
    # # Productos disponibles y con precio menor a 100
    # productos = Producto.objects.filter(disponible=True, precio__lt=100)
    # for product in productFilt:
    #     print(product.name, 'aqui****')
    # Filter ByID
    # productById =  Product.objects.get(id=1)
    # print(productById.name, '***')
    
    # order by results asc and desc
    # productos = Producto.objects.all().order_by('precio')        # Ascendente
    # productos = Producto.objects.all().order_by('-precio')       # Descendente

    
    return render(request, 'products/product_list.html',  {'products': products})

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
    
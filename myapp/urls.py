from django.urls import path
from .views import ( 
    TaskListCreateView, 
    TaskRetrieveUpdateDeleteView, 
    UserListCreateView, 
    UserRetrieveUpdateDestroyView, 
    create_product, 
    product_list, 
    crear_estudiante, 
    lista_estudiantes,
    editar_estudiante,
    eliminar_estudiante
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
    # step 4 configurate urls for request APIs of serializers 
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    
    #step 5 for create form with template
    #add route for forms and template
    path('crear/', create_product, name='create_product'),
    path('products/', product_list, name='product_list'),
    
    # Relaciones entre modelos (OneToMany, ManyToMany) con admin y formularios.
    # paso-6 crear URL para la vista
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/nuevo', crear_estudiante, name='crear_estudiante'),
    # complementando  para listar, editar, eliminar del modelo de estudiantes
    path('estudiantes/editar/<int:estudiante_id>', editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:estudiante_id>', eliminar_estudiante, name='eliminar_estudiante'),
    
]
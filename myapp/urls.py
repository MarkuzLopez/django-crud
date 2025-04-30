from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView, UserListCreateView, UserRetrieveUpdateDestroyView, create_product, product_list

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
]
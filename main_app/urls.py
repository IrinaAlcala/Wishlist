from django.urls import path
from . import views

urlpatterns = [
  
  path('', views.items_index, name='index'),
  path('items/<int:item_id>/', views.items_detail, name='detail'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  # path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
  path('delete/<int:item_id>', views.delete, name="delete"),
]
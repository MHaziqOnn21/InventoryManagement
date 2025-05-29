from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/<int:pk>', views.inventory_detail, name='inventory-detail'),
    path('inventory/new/', views.InventoryCreateView.as_view(), name='inventory-add'),
    path('inventory/<int:pk>/edit/', views.InventoryUpdateView.as_view(), name='inventory-edit'),
    path('inventory/<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory-delete')
]
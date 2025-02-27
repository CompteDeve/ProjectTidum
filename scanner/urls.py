from django.urls import path
from . import views
from .views import execute_scan

urlpatterns = [
    path('', views.scan_list, name='scan_list'),
    path('new/', views.scan_create, name='scan_create'),
    path('<int:pk>/edit/', views.scan_edit, name='scan_edit'),
    path('<int:pk>/delete/', views.scan_delete, name='scan_delete'),
    path('scan/<int:scan_id>/', execute_scan, name='scan_execute'),
]

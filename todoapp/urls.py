from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addTask, name='addtask'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
]

from django.urls import path
from .views import home, add_employee, edit_employee, delete_employee, EmployeeListCreateAPI, EmployeeDetailAPI

urlpatterns = [
    path('', home),
    path('add/', add_employee),
    path('edit/<int:id>/', edit_employee),
    path('delete/<int:id>/', delete_employee),
    path('api/employees/', EmployeeListCreateAPI.as_view()),
    path('api/employees/<int:pk>/', EmployeeDetailAPI.as_view()),
]

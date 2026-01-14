from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            designation=request.POST['designation'],
            salary=request.POST['salary'],
            date_joined=request.POST['date_joined'],
        )
        return redirect('/')
    return render(request, 'add_employee.html')

def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.designation = request.POST['designation']
        employee.salary = request.POST['salary']
        employee.date_joined = request.POST['date_joined']
        employee.save()
        return redirect('/')

    return render(request, 'edit_employee.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('/')

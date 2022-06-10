from rest_framework import serializers
from .models import Employee

from rest_framework import serializers


class EmployeeSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','employeeName','jobDescription','employeeNumber','employementDate','branch']

class EmployeeSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employeeName', 'jobDescription','employeeNumber','branch']

class EmployeeSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','employeeName','jobDescription','employementDate','branch']


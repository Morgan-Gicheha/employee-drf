
from .models import Employee
from rest_framework.decorators import api_view
from .serializers import  EmployeeSerializerGet,EmployeeSerializerPost,EmployeeSerializerPut
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

@api_view(['GET','POST'])
def allEmployees(request):
    if request.method == 'POST':
        # receiving post request
        serializer = EmployeeSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    allEmployees = Employee.objects.all()
    serializer = EmployeeSerializerGet(allEmployees, many=True)
    return JsonResponse({'response': serializer.data})


@api_view(['PUT','DELETE'])
def employeeModification(request,employeeNumber):
   
    try:
      
        employee = Employee.objects.filter(employeeNumber=employeeNumber) 
 
    except Employee.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
 
        serializer = EmployeeSerializerPut(employee.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)



        
    
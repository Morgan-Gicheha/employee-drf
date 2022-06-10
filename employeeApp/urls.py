
from django.contrib import admin
from django.urls import path
# importing all the views to register them
from employeeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('employees/', views.allEmployees),
     path('employees/<int:employeeNumber>', views.employeeModification),
]

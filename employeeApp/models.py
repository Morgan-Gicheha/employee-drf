
from django.db import models

from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")




class Employee(models.Model):
        employeeName = models.CharField(max_length=255)
        employeeNumber = models.IntegerField()
        jobDescription= models.TextField()
        employementDate = models.CharField(max_length=50, default=d1)
        branch = models.CharField(max_length=50)

# sqlite3 db.sqlite3' "select * from Employee;" ".exit"
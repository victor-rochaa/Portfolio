from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from accounts.models import Client, Employee
from pages.models import Category
# Create your models here.

class Services(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    job_date = models.DateField(null=True)
    job_time = models.TimeField(null=True)
    price = models.IntegerField(null=True)
    def __str__(self):
        return 'Cliente: %s - Prestador: %s' %(self.client.user_id, self.employee.user_id)

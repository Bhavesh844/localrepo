from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,employee
from api.serializers import comany_serializers,employee_serializers

# Create your views here.
class companyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=comany_serializers
    print(serializer_class)

class employeeViewSet(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employee_serializers

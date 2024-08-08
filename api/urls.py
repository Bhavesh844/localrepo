from django.urls import path,include
from rest_framework import routers
from api.views import companyViewSet,employeeViewSet

router=routers.DefaultRouter()
router.register(r'comapnies',companyViewSet)
router.register(r'employee',employeeViewSet)

urlpatterns = [
    path('',include(router.urls))
]

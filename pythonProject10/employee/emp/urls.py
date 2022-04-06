from django.urls import path, include
from . import views
from rest_framework import routers

from .views import EmployeeViewSet, DepartementViewset

router = routers.SimpleRouter()
router.register(r'department_post', DepartementViewset, basename="department_post")
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.index, name="home"),
    path("employee_post/", EmployeeViewSet.as_view(), name="employee_post"),
]

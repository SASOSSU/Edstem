from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async
# Create your views here.

# from utils.uniform_response import UniformResponse
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Employee, Department
from .serializer import EmyloyeeSerializer, DepartmentSerializer


def index(request):
    return HttpResponse("HAI")


class DepartementViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(generics.GenericAPIView):
    serializer_class = EmyloyeeSerializer

    @sync_to_async
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.add_profile(serializer.data)
            return Response(
                data={},
                status=status.HTTP_200_OK,

            )
        else:
            return Response(
                data={},
                status=status.HTTP_400_BAD_REQUEST,

            )

from rest_framework import generics

from clients.models import Client
from legal_entities.models import LegalEntity
from departments.models import Department

from .serializers import ClientSerializer, LegalEntitySerializer, DepartmentSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LegalEntityList(generics.ListCreateAPIView):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer

class LegalEntityDetail(generics.RetrieveAPIView):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer



class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
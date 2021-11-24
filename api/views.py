from rest_framework import generics
from clients.models import Client
from .serializers import ClientSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

from django.urls import path
from api.views import ClientList

urlpatterns =[
    path('clients/', ClientList.as_view(), name='clients_list'),
]
from django.urls import path
from api.views import ClientList, ClientDetail

urlpatterns =[
    path('clients/', ClientList.as_view(), name='clients_list'),
    path('clients/<int:pk>', ClientDetail.as_view(), name='clients_detail'),
]
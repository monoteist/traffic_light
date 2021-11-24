from django.urls import path
from api.views import ClientList, ClientDetail, LegalEntityDetail, LegalEntityList, DepartmentList, DepartmentDetail

urlpatterns = [
    path('clients/', ClientList.as_view(), name='clients_list'),
    path('clients/<int:pk>', ClientDetail.as_view(), name='client_detail'),
    path('legal_entities/', LegalEntityList.as_view(), name='legal_entities_list'),
    path('legal_entities/<int:pk>', LegalEntityDetail.as_view(),
         name='legal_entity_detail'),
    path('departments/', DepartmentList.as_view(), name='departments_list'),
    path('departments/<int:pk>', DepartmentDetail.as_view(), name='department_detail'),
]

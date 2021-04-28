from django.urls import path
from .views import (
    AddAdministration,
    ListAdministration,
    UpdateAdministration,
    DeleteAdministration,
    YearlyIncomeOutcomeProfitAdministration,
    MonthlyIncomeOutcomeProfitAdministration,
    GetAdministrationDetail
)

app_name = "administration"

urlpatterns = [
    path('addadministration/', AddAdministration.as_view(), name='addadministration'),
    path('listadministration/', ListAdministration.as_view(), name='listadministration'),
    path('updateadministration/<int:pk>/', UpdateAdministration.as_view(), name='updateadministration'),
    path('deleteadministration/', DeleteAdministration.as_view(), name='deleteadministration'),
    path(
        'administrationdataperyear/',
        YearlyIncomeOutcomeProfitAdministration.as_view(),
        name='administrationdataperyear'
    ),
    path(
        'administrationdatapermonth/',
        MonthlyIncomeOutcomeProfitAdministration.as_view(),
        name='administrationdatapermonth'
    ),
    path('administrationdetail/', GetAdministrationDetail.as_view(), name='administrationdetail')
]

from django.urls import path
from .views import TotalUser, TotalData, TotalDataToday

app_name = "information"

urlpatterns = [
    path('totaluser/', TotalUser.as_view(), name='totaluser'),
    path('totaldata/', TotalData.as_view(), name='totaldata'),
    path('totaldatatoday/', TotalDataToday.as_view(), name='totaldatatoday'),
]

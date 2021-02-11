from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.administration.models import Administration
import datetime


class TotalUser(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = User.objects.all().count()
        return Response({"total user": f"{user}"})


class TotalData(views.APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        total_data = Administration.objects.all().count()
        return Response({"total data": f"{total_data}"})


class TotalDataToday(views.APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        today = datetime.datetime.now()
        total_data_today = Administration.objects.filter(
            created_at=f"{today.year}-{today.month}-{today.day}"
        ).count()
        return Response({"total data today": f"{total_data_today}"})

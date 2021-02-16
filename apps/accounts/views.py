from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class StaffUser(views.APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        first_name = request.data.get("first name")
        last_name = request.data.get("last name")
        if username in [user.username for user in User.objects.all()]:
            return Response({"detail": "username already taken"})
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            return Response({"detail": "User successfully created"}, status=status.HTTP_201_CREATED)
from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from apps.administration.models import Administration
from apps.administration.serializers import AdministrationSerializer
from apps.administration.utils import get_all_administration_data


class AddAdministration(views.APIView):

    def post(self, request):
        if request.user.is_staff:
            tipe = request.data.get("tipe")
            nominal = request.data.get("nominal")
            deskripsi = request.data.get("deskripsi")
            bukti = request.data.get("bukti")
            created_at = request.data.get("created_at")

            Administration.objects.create(
                username=request.user.username,
                tipe=tipe,
                nominal=nominal,
                deskripsi=deskripsi,
                bukti=bukti,
                created_at=created_at
            )
            return Response({"detail": "Administration successfully created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Unauthorized request"}, status=status.HTTP_401_UNAUTHORIZED)


class ListAdministration(generics.ListAPIView):
    serializer_class = AdministrationSerializer

    def get_queryset(self):
        return Administration.objects.filter(username=self.request.user.username)


class UpdateAdministration(views.APIView):

    def post(self, request):
        administration_id = request.data.get("administration_id")
        if Administration.objects.get(id=administration_id).username == request.user.username:
            tipe = request.data.get("tipe")
            nominal = request.data.get("nominal")
            deskripsi = request.data.get("deskripsi")
            bukti = request.data.get("bukti")
            created_at = request.data.get("created_at")
            administration = Administration.objects.get(id=administration_id)
            administration.username = request.user.username
            administration.tipe = tipe
            administration.nominal = nominal
            administration.deskripsi = deskripsi
            administration.bukti = bukti
            administration.created_at = created_at
            administration.save()
            return Response({"detail": "Administration successfully updated"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Unauthorized request"}, status=status.HTTP_401_UNAUTHORIZED)


class DeleteAdministration(views.APIView):

    def delete(self, request):
        administration_id = request.data.get("administration_id")
        if Administration.objects.get(id=administration_id).username == request.user.username:
            administration = Administration.objects.get(id=administration_id)
            Administration.delete(administration)
            return Response({"detail": "Administration successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Unauthorized request"}, status=status.HTTP_401_UNAUTHORIZED)


class YearlyIncomeOutcomeProfitAdministration(views.APIView):

    def get(self, request):
        return Response(get_all_administration_data(request.user.username))


class MonthlyIncomeOutcomeProfitAdministration(views.APIView):

    def get(self, request):
        return Response(get_all_administration_data(request.user.username)[int(request.data.get("year"))])

from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from apps.administration.models import Administration
from apps.administration.serializers import AdministrationSerializer
from apps.administration.utils import get_all_administration_data, get_administration_detail


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

# class UpdateAdministration(generics.UpdateAPIView):
#     queryset = Administration.objects.all()
#     serializer_class = AdministrationSerializer


class DeleteAdministration(views.APIView):

    def delete(self, request):
        administration_id = request.GET.get("administration_id")
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
        return Response(get_all_administration_data(request.user.username)[int(request.GET.get("year"))])


class GetAdministrationDetail(views.APIView):

    def get(self, request):
        administration_detail = {}
        year = request.GET.get("year")
        month = request.GET.get("month")
        data = {}
        for administration_id in get_administration_detail("rafli")[2021][2]:
            data[administration_id] = Administration.objects.get(id=administration_id).created_at.day

        sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
        for x in sorted_data:
            obj = Administration.objects.get(id=x)
            administration_detail[x] = {}
            administration_detail[x]["tipe"] = obj.tipe
            administration_detail[x]["nominal"] = obj.nominal
            administration_detail[x]["deskripsi"] = obj.deskripsi
            if len(obj.bukti.name) == 0:
                administration_detail[x]["bukti"] = "None"
            else:
                administration_detail[x]["bukti"] = obj.bukti.url
            administration_detail[x]["created_at"] = f"{obj.created_at.year}-" \
                                                                     f"{obj.created_at.month}-" \
                                                             f"{obj.created_at.day}"
        return Response(administration_detail)

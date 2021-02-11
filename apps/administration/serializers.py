from rest_framework import serializers
from apps.administration.models import Administration


class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = "__all__"

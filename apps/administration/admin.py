from django.contrib import admin
from apps.administration.models import Administration


@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    list_display = ["username", "tipe", "nominal", "deskripsi", "bukti"]
    readonly_fields = ("username", )

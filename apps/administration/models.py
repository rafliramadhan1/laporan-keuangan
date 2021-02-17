from django.db import models
from apps.administration.choices import TipeChoices


class Administration(models.Model):
    username = models.CharField(max_length=50)
    tipe = models.CharField(
        max_length=20,
        choices=TipeChoices.choice,
    )
    nominal = models.IntegerField()
    deskripsi = models.TextField()
    bukti = models.FileField(upload_to="media/", null=True, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.tipe

    class Meta:
        verbose_name_plural = "Administration"

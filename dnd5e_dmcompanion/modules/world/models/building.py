from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class Building(PolymorphicModel):
    district = models.ForeignKey(
        "world.District",
        on_delete=models.CASCADE,
        related_name="buildings",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="buildings", blank=True, null=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "character.Character",
        on_delete=models.CASCADE,
        related_name="buildings",
        blank=True,
        null=True,
    )
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")

    def __str__(self):
        return self.name

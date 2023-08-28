from django.db import models
from django.utils.translation import gettext_lazy as _


class District(models.Model):
    city = models.ForeignKey(
        "world.City",
        on_delete=models.CASCADE,
        related_name="districts",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="districts", blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def __str__(self):
        return self.name

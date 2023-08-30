from django.db import models
from django.utils.translation import gettext_lazy as _


class World(models.Model):
    campaign = models.ForeignKey(
        "campaign.Campaign",
        on_delete=models.CASCADE,
        related_name="worlds",
        blank=True,
        null=True,
    )
    map = models.ImageField(upload_to="worlds", blank=True, null=True)
    image = models.ImageField(upload_to="worlds", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    dm = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name="worlds",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("World")
        verbose_name_plural = _("Worlds")

    def __str__(self):
        if self.campaign:
            return f"{self.campaign} - run by {self.dm}"
        return f"A homebrew world run by {self.dm}"

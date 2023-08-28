from django.db import models
from django.utils.translation import gettext_lazy as _


class NotableEvent(models.Model):
    world = models.ForeignKey(
        "world.World",
        on_delete=models.CASCADE,
        related_name="notable_events",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="notable_events", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Notable Event")
        verbose_name_plural = _("Notable Events")

    def __str__(self):
        return f"Notable event in {self.world} from {self.created_at.strftime('%Y-%m-%d %H:%M')}"

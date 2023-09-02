from django.db import models
from django.utils.translation import gettext_lazy as _


class Kingdom(models.Model):
    council = models.ForeignKey(
        "character.CharacterGroup",
        on_delete=models.CASCADE,
        related_name="kingdoms_council",
        blank=True,
        null=True,
    )
    leader = models.ForeignKey(
        "character.Character",
        on_delete=models.CASCADE,
        related_name="kingdoms_leader",
        blank=True,
        null=True,
    )
    map = models.ImageField(upload_to="kingdoms", blank=True, null=True)
    name = models.CharField(max_length=255)
    world = models.ForeignKey(
        "world.World",
        on_delete=models.CASCADE,
        related_name="kingdoms",
        blank=True,
        null=True,
    )
    army = models.ForeignKey(
        "character.CharacterGroup",
        on_delete=models.CASCADE,
        related_name="kingdoms_army",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Kingdom")
        verbose_name_plural = _("Kingdoms")

    def __str__(self):
        return self.name

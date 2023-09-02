from django.db import models
from django.utils.translation import gettext_lazy as _

from polymorphic.models import PolymorphicModel


class CharacterGroup(PolymorphicModel):
    name = models.CharField(max_length=100)

    type = models.CharField(max_length=100)
    worlds = models.ManyToManyField(
        "world.World",
        related_name="groups",
        blank=True,
    )
    base = models.ForeignKey(
        "world.Building",
        related_name="groups",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    founders = models.ManyToManyField(
        "character.Character",
        related_name="groups",
        blank=True,
    )

    total_members = models.IntegerField(default=0)
    known_members = models.ManyToManyField(
        "character.Character",
        related_name="known_groups",
        blank=True,
    )
    allies = models.ManyToManyField(
        "character.CharacterGroup",
        related_name="allies_groups",
        blank=True,
    )
    emblem = models.ImageField(upload_to="emblems/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Character Group")
        verbose_name_plural = _("Character Groups")

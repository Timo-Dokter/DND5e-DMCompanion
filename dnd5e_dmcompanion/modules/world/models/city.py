from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    council = models.ForeignKey(
        "character.CharacterGroup",
        on_delete=models.CASCADE,
        related_name="cities",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True, null=True)
    guard_force = models.ForeignKey(
        "character.CharacterGroup",
        on_delete=models.CASCADE,
        related_name="cities_guarded",
        blank=True,
        null=True,
    )
    is_capital = models.BooleanField(default=False)
    kingdom = models.ForeignKey(
        "world.Kingdom",
        on_delete=models.CASCADE,
        related_name="cities",
        blank=True,
        null=True,
    )
    leader = models.ForeignKey(
        "character.Character",
        on_delete=models.CASCADE,
        related_name="cities",
        blank=True,
        null=True,
    )
    map = models.ImageField(upload_to="cities", blank=True, null=True)
    name = models.CharField(max_length=255)
    notable_character_groups = models.ManyToManyField(
        "character.CharacterGroup",
        related_name="notable_character_groups",
        blank=True,
    )
    notable_characters = models.ManyToManyField(
        "character.Character",
        related_name="notable_characters",
        blank=True,
    )
    population = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name

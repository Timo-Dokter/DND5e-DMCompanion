from django.db import models
from django.utils.translation import gettext_lazy as _


class Ship(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(
        "character.Character", on_delete=models.SET_NULL, null=True
    )
    crew = models.ManyToManyField("character.Character", related_name="crewed_ships")
    max_crew_capacity = models.PositiveIntegerField()
    cargo_capacity = models.DecimalField(max_digits=10, decimal_places=2)  # In tons
    current_cargo = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )  # In tons
    speed = models.PositiveIntegerField()  # Speed of the ship in knots
    hull_strength = models.PositiveIntegerField()  # Hull strength points
    armament = models.ManyToManyField(
        "world.ShipWeapon", related_name="equipped_on_ships"
    )
    items = models.ManyToManyField("item.Item", related_name="aboard_ships")
    location = models.CharField(max_length=100)  # Current location of the ship

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Ship")
        verbose_name_plural = _("Ships")

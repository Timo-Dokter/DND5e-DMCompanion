from django.db import models
from django.utils.translation import gettext_lazy as _


class ShipWeapon(models.Model):
    name = models.CharField(max_length=100)
    damage = models.CharField(max_length=20)
    range = models.CharField(max_length=20)
    damage_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Weapon")
        verbose_name_plural = _("Weapons")

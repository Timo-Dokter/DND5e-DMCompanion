from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    DAMAGE_TYPES = (
        ("acid", _("Acid")),
        ("bludgeoning", _("Bludgeoning")),
        ("cold", _("Cold")),
        ("fire", _("Fire")),
        ("force", _("Force")),
        ("lightning", _("Lightning")),
        ("necrotic", _("Necrotic")),
        ("piercing", _("Piercing")),
        ("poison", _("Poison")),
        ("psychic", _("Psychic")),
        ("radiant", _("Radiant")),
        ("slashing", _("Slashing")),
        ("thunder", _("Thunder")),
    )
    DURATION_TYPES = (
        ("instantaneous", _("Instantaneous")),
        ("round", _("Round")),
        ("minute", _("Minute")),
        ("hour", _("Hour")),
        ("day", _("Day")),
        ("week", _("Week")),
        ("month", _("Month")),
        ("year", _("Year")),
        ("permanent", _("Permanent")),
    )
    PRICE_TYPES = (
        ("cp", _("Copper")),
        ("sp", _("Silver")),
        ("ep", _("Electrum")),
        ("gp", _("Gold")),
        ("pp", _("Platinum")),
    )
    RARITIES = (
        ("common", _("Common")),
        ("uncommon", _("Uncommon")),
        ("rare", _("Rare")),
        ("very_rare", _("Very Rare")),
        ("legendary", _("Legendary")),
        ("artifact", _("Artifact")),
    )

    armor_class = models.PositiveIntegerField(blank=True, null=True)
    base_item = models.CharField(max_length=255, blank=True, null=True)
    damage = models.CharField(max_length=255, blank=True, null=True)
    damage_type = models.CharField(
        max_length=255, choices=DAMAGE_TYPES, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveBigIntegerField(blank=True, null=True)
    duration_type = models.CharField(
        max_length=255, choices=DURATION_TYPES, blank=True, null=True
    )
    image = models.ImageField(upload_to="items", blank=True, null=True)
    magic_item = models.BooleanField(default=False)
    max_charges = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=True, null=True)
    price_type = models.CharField(
        max_length=255, choices=PRICE_TYPES, blank=True, null=True
    )
    properties = models.ManyToManyField(
        "item.ItemProperty", related_name="items", blank=True
    )
    range = models.PositiveIntegerField(blank=True, null=True)
    rarity = models.CharField(max_length=255, choices=RARITIES, blank=True, null=True)
    recharge_rate = models.PositiveIntegerField(blank=True, null=True)
    recharge_type = models.CharField(
        max_length=255, choices=DURATION_TYPES, blank=True, null=True
    )
    requires_attunement = models.BooleanField(default=False)
    save_dc = models.PositiveIntegerField(blank=True, null=True)
    save_type = models.ForeignKey(
        "character.AbilityScore",
        on_delete=models.CASCADE,
        related_name="items",
        blank=True,
        null=True,
    )
    type = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

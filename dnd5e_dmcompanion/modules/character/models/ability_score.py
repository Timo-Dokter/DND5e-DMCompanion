from django.db import models
from django.utils.translation import gettext_lazy as _


class AbilityScore(models.Model):
    """
    Model for AbilityScore
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Ability Score")
        verbose_name_plural = _("Ability Scores")

    def __str__(self):
        return self.name

from django.db import models

from django.utils.translation import gettext_lazy as _


class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    reward = models.CharField(max_length=100)
    penalty = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Goal")
        verbose_name_plural = _("Goals")

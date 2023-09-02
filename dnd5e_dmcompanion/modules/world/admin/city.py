from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from dnd5e_dmcompanion.modules.world.models import City


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ("__str__",)

    search_fields = ("name",)

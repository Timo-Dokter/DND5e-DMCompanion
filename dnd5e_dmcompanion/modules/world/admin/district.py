from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from dnd5e_dmcompanion.modules.world.models import District
from dnd5e_dmcompanion.modules.world.admin.buildings import ShopInline


@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)
    # inlines = (ShopInline,)

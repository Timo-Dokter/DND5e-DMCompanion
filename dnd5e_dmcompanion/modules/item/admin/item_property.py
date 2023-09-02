from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _

from dnd5e_dmcompanion.modules.item.models import ItemProperty


@admin.register(ItemProperty)
class ItemPropertyAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                )
            },
        ),
    )

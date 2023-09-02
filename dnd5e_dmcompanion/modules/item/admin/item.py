from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _


from dnd5e_dmcompanion.modules.item.models import Item, ItemTrait, ItemModifier


class ItemTraitInline(admin.TabularInline):
    model = ItemTrait
    extra = 0


class ItemModifierInline(admin.TabularInline):
    model = ItemModifier
    extra = 0


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = (
        "__str__",
        "base_item",
        "magic_item",
        "get_price",
        "weight",
        "armor_class",
        "get_range",
        "damage",
        "damage_type",
        "description",
    )
    list_filter = (
        "magic_item",
        "type",
    )
    search_fields = ("name",)
    inlines = (ItemTraitInline, ItemModifierInline)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "base_item",
                    "magic_item",
                    "price",
                    "price_type",
                    "weight",
                    "armor_class",
                    "damage",
                    "damage_type",
                    "description",
                    "duration",
                    "duration_type",
                    "image",
                    "max_charges",
                    "range",
                    "rarity",
                    "recharge_rate",
                    "recharge_type",
                    "requires_attunement",
                    "save_dc",
                    "save_type",
                    "type",
                ),
            },
        ),
        (
            _("Additional Information"),
            {
                "fields": ("properties",),
            },
        ),
    )

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin
from polymorphic.admin import StackedPolymorphicInline

from dnd5e_dmcompanion.modules.world.models import Shop


@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ("__str__",)
    search_fields = ("name",)


class ShopInline(StackedPolymorphicInline):
    model = Shop
    fields = ("name",)
    extra = 0
    classes = ("collapse",)
    show_change_link = True
    verbose_name = _("Shop")
    verbose_name_plural = _("Shops")

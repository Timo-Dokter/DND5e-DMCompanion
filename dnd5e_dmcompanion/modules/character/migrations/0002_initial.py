# Generated by Django 4.2.4 on 2023-09-02 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("world", "0001_initial"),
        ("character", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="charactergroup",
            name="base",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                to="world.building",
            ),
        ),
        migrations.AddField(
            model_name="charactergroup",
            name="founders",
            field=models.ManyToManyField(
                blank=True, related_name="groups", to="character.character"
            ),
        ),
        migrations.AddField(
            model_name="charactergroup",
            name="known_members",
            field=models.ManyToManyField(
                blank=True, related_name="known_groups", to="character.character"
            ),
        ),
        migrations.AddField(
            model_name="charactergroup",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_%(app_label)s.%(class)s_set+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="charactergroup",
            name="worlds",
            field=models.ManyToManyField(
                blank=True, related_name="groups", to="world.world"
            ),
        ),
    ]

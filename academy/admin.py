from django.contrib import admin

# Register your models here.
from .models import Planet, Jedi, Сandidate


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

    list_display_links = (
        'title',
    )

    # list_filter = (
    # )


@admin.register(Jedi)
class JediAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
        'grade',
    )

    list_display_links = (
        'name',
    )


@admin.register(Сandidate)
class СandidateAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "habitat_planet",
        "email",
    )

    list_display_links = (
        'name',
    )
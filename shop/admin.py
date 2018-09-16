from django.contrib import admin

from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand admin."""


@admin.register(models.Hat)
class HatAdmin(admin.ModelAdmin):
    """Hat admin."""


@admin.register(models.Footwear)
class FootwearAdmin(admin.ModelAdmin):
    """Footwear admin."""


@admin.register(models.FootwearStyle)
class FootwearStyleAdmin(admin.ModelAdmin):
    """Footwear admin."""


@admin.register(models.HatStyle)
class HatStyleAdmin(admin.ModelAdmin):
    """Footwear admin."""

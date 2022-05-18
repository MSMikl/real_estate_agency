from django.contrib import admin

from .models import Flat, Like, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['likes']
    inlines = [OwnerInline]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
    exclude = ['flats']

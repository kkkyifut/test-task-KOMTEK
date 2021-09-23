from django.contrib import admin

from .models import HandBook, Item


class HandBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'name', 'description', 'version', 'pub_date')
    search_fields = ('text', 'description',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'handbook', 'code', 'value')
    search_fields = ('handbook', 'code', 'value',)
    list_filter = ('handbook', 'code', 'value',)
    empty_value_display = '-пусто-'


admin.site.register(HandBook, HandBookAdmin)
admin.site.register(Item, ItemAdmin)

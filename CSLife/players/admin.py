from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.site_title = 'Админ-панель сайта о CS GO'
admin.site.site_header = 'Админ-панель сайта о CS GO'


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'name', 'country', 'get_html_photo', 'team')
    list_display_links = ('nickname',)
    search_fields = ('nickname', 'information')
    list_editable = ('team',)
    list_filter = ('country', 'team')
    prepopulated_fields = {"slug": ("nickname",)}
    readonly_fields = ('get_html_photo', )
    fields = ('nickname', 'name', 'country', 'age', 'information',  'photo', 'get_html_photo', 'team', 'slug')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Photo"


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'coach', 'get_html_logo')
    list_display_links = ('name',)
    search_fields = ('name', 'information')
    list_editable = ('coach',)
    list_filter = ('country',)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('get_html_logo',)
    fields = ('name', 'country', 'coach', 'information', 'logo', 'get_html_logo', 'slug')

    def get_html_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' width=50>")
        else:
            return "Нет логотипа"

    get_html_logo.short_description = "Logo"

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)

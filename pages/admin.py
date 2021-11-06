from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40px" style="border-radius: 50px" />')

    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date',)
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('first_name', 'last_name', 'designation', 'created_date',)
    list_filter = ('designation', 'created_date',)

admin.site.register(Team, TeamAdmin)

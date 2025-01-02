from django.contrib import admin

from .models import Link, Group
from .models import (
    NewsContent,
    NewsPost,
)


class NewsContentInline(admin.TabularInline):
    model = NewsContent
    extra = 1


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]
    inlines = [NewsContentInline]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')
    search_fields = ('title', 'url')


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    list_display = ('name', 'created_at')
    search_fields = ('name',)

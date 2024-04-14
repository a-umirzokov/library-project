from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'published']
    list_filter = ['published']
    search_fields = ['title', 'description']
    list_editable = ['price']
    list_per_page = 10
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(published=True)
    make_published.short_description = 'Mark selected books as published'

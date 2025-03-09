from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_datetime', 'thumbnail_preview', 'created_at')
    list_filter = ('publication_datetime', 'author')
    search_fields = ('title', 'description', 'author')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug from title
    readonly_fields = ('thumbnail_preview',)  # Show thumbnail preview
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'content')
        }),
        ('Publication Details', {
            'fields': ('publication_datetime','author'),
            'classes': ('collapse',)
        }),
        ('Thumbnail', {
            'fields': ('thumbnail', 'thumbnail_preview'),
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" width="100" height="100" style="border-radius: 10px;" />')
        return "No Image"
    
    thumbnail_preview.short_description = "Thumbnail Preview"

admin.site.register(Blog, BlogAdmin)

admin.site.register(Project)

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_datetime', 'thumbnail_preview', 'created_at')
    list_filter = ('publication_datetime', 'author')
    search_fields = ('title', 'description', 'author')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug from title
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'content')
        }),
        ('Publication Details', {
            'fields': ('publication_datetime','author'),
            'classes': ('collapse',)
        }),
       
    )

    

admin.site.register(Blog, BlogAdmin)

admin.site.register(Project)

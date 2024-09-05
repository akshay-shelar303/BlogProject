from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "user"]


admin.site.register(Blog, BlogAdmin)

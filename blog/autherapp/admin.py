from django.contrib import admin

from .models import Auther, ThreadPost


class AutherAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age"]


admin.site.register(Auther, AutherAdmin)


class ThreadPostAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created_at", "likes"]


admin.site.register(ThreadPost, ThreadPostAdmin)

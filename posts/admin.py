from django.contrib import admin
from .models import *

admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'category',
        'mediafile'
    )
    search_fields = (
        'title',
    )


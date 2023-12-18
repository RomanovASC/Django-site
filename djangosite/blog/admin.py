from .models import Post, Tag
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', '_tag')
    list_filter = ('status', 'created', 'publish', 'author', 'tags')
    search_fields = ('title', 'body', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    autocomplete_fields = ('tags',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    def _tag(self, obj):
        return ", ".join(tag.tag_name for tag in obj.tags.all())


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name',)


admin.site.register(Tag, TagAdmin)
from django.contrib import admin

# Register your models here.
from .models import Category, Post, Tag, Comment

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'tag_name')
    search_fields = ['tag_name']

admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'cat_cod', 'cat_name', 'cat_parent_id', 'cat_desc', 'cat_flg_active')
    list_filter = ("cat_flg_active",)
    search_fields = ['cat_cod', 'cat_name', 'cat_desc']

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("post_status", "post_flg_active")
    search_fields = ['post_title', 'post_content']
    prepopulated_fields = {'post_slug': ('post_title',)}

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("com_status", "com_flg_active")
    search_fields = ['com_content']

admin.site.register(Comment, CommentAdmin)

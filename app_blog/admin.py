from django.contrib import admin

# Register your models here.
from .models import Category 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id', 'cat_cod', 'cat_name','cat_parent_id')
    #list_filter = ("status",)
    search_fields = ['cat_cod', 'cat_name']
    #prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Category, CategoryAdmin)

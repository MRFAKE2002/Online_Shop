from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name', 'slug', 'has_parent', 'available')
    
    search_fields = ('name', 'slug', 'parent')
    
    list_filter = ('available', 'datetime_create')
    
    list_editable = ('has_parent', 'available',)
    
    prepopulated_fields = { "slug" : ['name']}
    
    list_select_related = ('parent',)
    
    list_per_page = 10
    
    ordering = ('id', 'name')


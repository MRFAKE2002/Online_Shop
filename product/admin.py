from django.contrib import admin
from django.db.models import Count, Subquery, OuterRef
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _

from .models import Product, ProductImages, Variant, Color, Size

import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category', 'price', 'status', 'is_active', 'product_images_count_column', 'product_variants_count_column')
    
    search_fields = ('name', 'slug', 'content')
    
    list_filter = ('status', 'is_active', 'datetime_created')
    
    list_editable = ('price', 'status', 'is_active')
    
    list_select_related = ('category',)
    
    prepopulated_fields = { "slug" : ['name']}
    
    list_per_page = 10
    
    ordering = ('id',)

    inlines = [
        ProductImagesInline,
        VariantInline,
    ]
    
    
    def get_queryset(self, request):
        # Annotate with counts of related ProductImage instances and ProductVariant instances
        queryset = super().get_queryset(request).annotate(
            product_images_count=Subquery(
                ProductImages.objects.filter(product_id=OuterRef('id')).values('product_id').annotate(
                    count=Count('product_id')).values('count'),
                output_field=models.IntegerField()
            ),
            product_variants_count=Subquery(
                Variant.objects.filter(product_id=OuterRef('id')).values('product_id').annotate(
                    count=Count('product_id')).values('count'),
                output_field=models.IntegerField()
            ),
        )
        return queryset
    
    
    @admin.display(ordering="product_images_count", description=_("# images"))
    def product_images_count_column(self, product=Product):
        """
            We use this method to get the number of product`s images in the changelist.
        """
        url = (
            reverse("admin:product_productimages_changelist")
            + "?"
            + urlencode({
                "product" : product.id,
            })
        )
        return format_html('<a href="{}" >{}</a>', url, product.product_images_count)
    
    
    @admin.display(ordering="product_variants_count", description=_("# variants"))
    def product_variants_count_column(self, product=Product):
        """
            We use this method to get the number of product`s variants in the changelist.
        """
        url = (
            reverse("admin:product_variant_changelist")
            + "?"
            + urlencode({
                "product" : product.id,
            })
        )
        return format_html('<a href="{}" >{}</a>', url, product.product_variants_count)


@admin.register(ProductImages)
@admin_thumbnails.thumbnail('image')
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_thumbnail', 'product', 'name', )
    
    search_fields = ('name', 'product',)
    
    list_select_related = ('product',)
    
    prepopulated_fields = { "name" : ['product']}
    
    list_per_page = 10
    
    ordering = ('id',)
    
    def lookup_allowed(self, key, value):
        """
            We must override this method to use product as filter for show the product_images by using product_images_count_column method.
        """
        if key in ('product'):
            return True
        return super(ProductAdmin, self).lookup_allowed(key, value)
    


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'price', 'discount', 'inventory')
    
    search_fields = ('product', 'color', 'size')
        
    list_select_related = ('product', 'color', 'size')
        
    list_per_page = 10
    
    ordering = ('id',)
    
    def lookup_allowed(self, key, value):
        """
            We must override this method to use product as filter for show the product_images by using product_images_count_column method.
        """
        if key in ('product'):
            return True
        return super(ProductAdmin, self).lookup_allowed(key, value)
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    search_fields = ('name',)
                
    list_per_page = 10
    
    ordering = ('id',)
    
    

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    search_fields = ('name',)
                
    list_per_page = 10
    
    ordering = ('id',)
    
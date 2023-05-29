from django.contrib import admin

from .models import*

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Seller)

class ProductImageAdmin(admin.TabularInline):
    model=ProductImage
    extra=1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]
    list_display=["title","price","discount_price","product_type","warranty_period","brand","category","seller"]
    list_editable=["discount_price","price"]
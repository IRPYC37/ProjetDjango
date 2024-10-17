from django.contrib import admin
from .models import Product, ProductItem, ProductAttribute, ProductAttributeValue, Supplier, ProductSupplier, Order, OrderItem

def set_product_online(modeladmin, request, queryset):
    queryset.update(status='online')

set_product_online.short_description = "Mettre en ligne"

def set_product_offline(modeladmin, request, queryset):
    queryset.update(status='offline')

set_product_offline.short_description = "Mettre hors ligne"

class ProductItemAdmin(admin.TabularInline):
    model = ProductItem

class ProductFilter(admin.SimpleListFilter):
    title = 'Product Filter'
    parameter_name = 'product'

    def lookups(self, request, model_admin):
        return [
            ('online', 'Online'),
            ('offline', 'Offline'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'online':
            return queryset.filter(status='online')
        if self.value() == 'offline':
            return queryset.filter(status='offline')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price_ht', 'price_ttc', 'date_creation')
    list_filter = (ProductFilter,)
    list_editable = ('price_ht', 'price_ttc')
    date_hierarchy = 'date_creation'
    actions = [set_product_online, set_product_offline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(Supplier)
admin.site.register(ProductSupplier)
admin.site.register(Order)
admin.site.register(OrderItem)
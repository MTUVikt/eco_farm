from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title', ]}
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'aviable', 'created', 'updated', 'amount', 'price']
    list_filter = ['category', 'aviable']
    list_editable = ['aviable', 'amount', 'price']
    prepopulated_fields = {'slug': ['title', ]}
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

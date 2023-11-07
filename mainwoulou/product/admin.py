from django.contrib import admin

# Register your models here.


from .models import Product
from .models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    search_fields = ("name",)
    list_display = ("id", "name", "slug")



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ("name",)

    list_display = (
        "name",
        "category",
    )
    list_filter = (("category", admin.RelatedOnlyFieldListFilter),)


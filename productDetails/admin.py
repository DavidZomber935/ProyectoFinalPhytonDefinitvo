from django.contrib import admin
from .models import Gender, ProductDetails

# Register your models here.
class GenderAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Gender, GenderAdmin)

class ProductDetailsAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author',)
    search_fields=('title','review','author__username','genders__name')
    list_filter=('author__username','genders__name',)
admin.site.register(ProductDetails, ProductDetailsAdmin)

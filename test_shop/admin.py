from django.contrib import admin
from .models import Product, Status


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'art', 'price', 'status', 'image')


class StatusProductAdmin(admin.ModelAdmin):
    fields = ('status_value',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Status, StatusProductAdmin)

from django.contrib import admin
from.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
      list_display = ('name', 'stock', 'price','date_created')
    #   list_filter = ('category',)
    #   search_fields = ('name',)
admin.site.register(Product,ProductAdmin)

from django.contrib import admin
import shop.models as models

admin.site.register(models.Product)
admin.site.register(models.Blog)
admin.site.register(models.CartItem)

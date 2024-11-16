from django.contrib import admin
from .models import customer,Product,Orders,Feedback

# Register your models here.

class customerAdmin(admin.ModelAdmin):
    pass
admin.site.register(customer, customerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)

# Register your models here.

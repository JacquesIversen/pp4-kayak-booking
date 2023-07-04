from django.contrib import admin
from .models import KayakVariant, Duration, OrderModel

# Register your models here.


admin.site.register(KayakVariant)
admin.site.register(Duration)
admin.site.register(OrderModel)
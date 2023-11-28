from django.contrib import admin

from .models import Vendor_Model,Purchase_Order_Model,Historical_Performance_Model
admin.site.register(Vendor_Model)
admin.site.register(Purchase_Order_Model)
admin.site.register(Historical_Performance_Model)

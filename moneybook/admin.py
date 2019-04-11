from django.contrib import admin

# Register your models here.
from .models import ExpenditureDetail, ReceiptImage

admin.site.register(ExpenditureDetail)
admin.site.register(ReceiptImage)

from django.contrib import admin

# Register your models here.
from core.operations.models import Invoice, Operation, Payment


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentnAdmin(admin.ModelAdmin):
    pass
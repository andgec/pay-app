from django.contrib import admin
from .models import Customer, SalesInvoiceJournal
#from shared.models import Address
'''
class AddressInline(admin.TabularInline):
    model = Address.customer

class CustomerAdmin(admin.ModelAdmin):
    inlines = (AddressInline,)
'''
admin.site.register(Customer)
admin.site.register(SalesInvoiceJournal)

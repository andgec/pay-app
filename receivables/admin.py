from django.contrib import admin
from .models import Customer, SalesInvoiceJournal

#class SalesInvoiceJournalAdmin(admin.ModelAdmin):
#    fields = ('created', 'year', 'month', 'amount', 'half_amount', 'attachment')    

#admin.site.register(SalesInvoiceJournal, SalesInvoiceJournalAdmin)
admin.site.register(Customer)
admin.site.register(SalesInvoiceJournal)

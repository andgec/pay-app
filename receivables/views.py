from django.shortcuts import render
from .models import SalesInvoiceJournal

def sales_invoice_journal(request):
    journal = SalesInvoiceJournal.objects.all()
    return render(request, 'receivables/sales_invoice_journal.html', {'journal': journal})
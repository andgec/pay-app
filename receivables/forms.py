from django import forms
from .models import SalesInvoiceJournal

class SalesInvoiceJournalForm(forms.ModelForm):
    class Meta:
        model = SalesInvoiceJournal
        fields = ('year', 'month', 'amount', 'attachment')
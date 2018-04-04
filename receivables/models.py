from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from _datetime import datetime
from django.conf import settings
from shared.const import MONTH_CHOICES
from django.db.models.fields import CharField, PositiveSmallIntegerField
from general.models import Address
from django.db.models.deletion import PROTECT

COMPANY = 100
PERSON  = 200

CUSTOMER_TYPE_CHOICES = (
        (COMPANY, _('Company')),
        (PERSON, _('Person')),
    )

class Customer(models.Model):
    number = CharField(max_length=32, unique=True)
    name = CharField(max_length=128)
    type = PositiveSmallIntegerField(choices=CUSTOMER_TYPE_CHOICES, default=COMPANY)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=PROTECT, related_name='customer')
    shipping_address = models.ForeignKey(Address, blank=True, null=True, on_delete=PROTECT, related_name='customer_ship')
    billing_address = models.ForeignKey(Address, blank=True, null=True, on_delete=PROTECT, related_name='customer_bill')
    
    def __str__(self):
        return self.number + ' - ' + self.name

class SalesInvoiceJournal(models.Model):
    created = models.DateTimeField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2100)])
    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES
        )
    amount = models.DecimalField(max_digits=settings.DECIMAL_FIELD_MAX_DIGITS,
                                 decimal_places=settings.DECIMAL_FIELD_DECIMAL_PLACES)
    def _get_half_amount(self):
        #return self.amount/2
        return 'kr. {:0,.2f}'.format(self.amount/2)
    half_amount=property(_get_half_amount)

    def _get_invoice_period(self):
        return str(self.year) + ' ' + str(MONTH_CHOICES[self.month - 1][1])

    invoice_period = property(_get_invoice_period)

    attachment = models.FileField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _('Sales Invoice Journal')
    
    def __str__(self):
        return str(self.year) + ' ' + str(MONTH_CHOICES[self.month - 1][1]) + ', kr. {:0,.2f}'.format(self.amount).replace('kr-','-kr')



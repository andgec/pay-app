from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from _datetime import datetime
from django.conf import settings

class PurchaseInvoiceJournal(models.Model):
    JANUARY     = 1
    FEBRUARY    = 2
    MARCH       = 3
    APRIL       = 4
    MAY         = 5
    JUNE        = 6
    JULY        = 7
    AUGUST      = 8
    SEPTEMBER   = 9
    OCTOBER     = 10
    NOVEMBER    = 11
    DECEMBER    = 12

    MONTH_CHOICES = (
        (JANUARY,   _('Sausis')),
        (FEBRUARY,  _('Vasaris')),
        (MARCH,     _('Kovas')),
        (APRIL,     _('Balandis')),
        (MAY,       _('Gegužė')),
        (JUNE,      _('Birželis')),
        (JULY,      _('Liepa')),
        (AUGUST,    _('Rugpjūtis')),
        (SEPTEMBER, _('Rugsėjis')),
        (OCTOBER,   _('Spalis')),
        (NOVEMBER,  _('Lapkritis')),
        (DECEMBER,  _('Gruodis')),
    )

    created = models.DateTimeField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2100)])
    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES
        )
    amount = models.DecimalField(max_digits=settings.DECIMAL_FIELD_MAX_DIGITS,
                                 decimal_places=settings.DECIMAL_FIELD_DECIMAL_PLACES)
    attachment = models.FileField()
    
    class Meta:
        verbose_name_plural = _('Purchase Invoice Journal')
    
    def __str__(self):
        return str(self.year) + ' ' + str(self.MONTH_CHOICES[self.month - 1][1]) + ', kr. {:0,.2f}'.format(self.amount).replace('kr-','-kr')
    

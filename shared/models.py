from django.db import models
from django_countries.fields import CountryField
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import ugettext_lazy as _


class AddressMixin(models.Model):
    '''
    A mixin class that adds address information fields and methods
    '''
    address     = models.CharField(max_length=100, blank=True, default='')
    address2    = models.CharField(max_length=100, blank=True, default='')
    city        = models.CharField(max_length=60, blank=True, default='')
    post_code   = models.CharField(max_length=16, blank=True, default='')
    country     = CountryField(blank_label=_('(select country)'), blank=True)

    class Meta:
        abstract = True

class ContactMixin(models.Model):
    '''
    A mixin class that adds contact information fields and methods
    '''
    first_name  = models.CharField(max_length=60)
    last_name   = models.CharField(max_length=60, blank=True, default='')
    email       = models.EmailField(max_length=120, blank=True, default='')
    phone_no    = models.CharField(max_length=20, blank=True, default='')
    web_site    = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        abstract = True

class Address(ContactMixin, AddressMixin, models.Model):
    class Meta:
        abstract = False
    def __str__(self):
        return self.address
        
    
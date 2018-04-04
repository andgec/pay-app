from django.db import models
from shared.models import AddressMixin, ContactMixin, ExtendedAddressMixin

class Contact(ContactMixin, AddressMixin, models.Model):
    first_name  = models.CharField(max_length=60)
    last_name   = models.CharField(max_length=60, blank=True, default='')
    
    def __str__(self):
        return self.first_name + ' - ' + self.last_name

class Address(ContactMixin, AddressMixin, models.Model):
    class Meta:
        abstract = False
    def __str__(self):
        return self.address

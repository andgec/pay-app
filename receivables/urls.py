from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sales_invoice_journal, name='post-list'),
]
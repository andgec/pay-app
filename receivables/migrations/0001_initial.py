# Generated by Django 2.0 on 2018-01-21 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoiceJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'Sausis'), (2, 'Vasaris'), (3, 'Kovas'), (4, 'Balandis'), (5, 'Gegužė'), (6, 'Birželis'), (7, 'Liepa'), (8, 'Rugpjūtis'), (9, 'Rugsėjis'), (10, 'Spalis'), (11, 'Lapkritis'), (12, 'Gruodis')])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('attachment', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Sales Invoice Journal',
            },
        ),
    ]

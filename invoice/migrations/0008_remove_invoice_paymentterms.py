# Generated by Django 4.0.1 on 2022-01-14 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_invoice_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paymentTerms',
        ),
    ]
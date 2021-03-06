# Generated by Django 4.0.1 on 2022-01-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_remove_invoice_paymentterms'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='paymentTerms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('CURRENT', 'در جریان'), ('ایمیل ارسال شد', 'ایمیل ارسال شد'), ('عقب افتاده', 'عقب افتاده'), ('پرداخت شده', 'پرداخت شده')], default='CURRENT', max_length=100),
        ),
    ]

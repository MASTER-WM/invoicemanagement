# Generated by Django 4.0.1 on 2022-01-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_alter_invoice_paymentterms_alter_invoice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('در جریان', 'در جریان'), ('ایمیل ارسال شد', 'ایمیل ارسال شد'), ('عقب افتاده', 'عقب افتاده'), ('پرداخت شده', 'پرداخت شده')], default='CURRENT', max_length=100),
        ),
    ]

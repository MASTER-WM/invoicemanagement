# Generated by Django 4.0.1 on 2022-01-20 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0016_rename_titile_invoice_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='invoice',
        ),
        migrations.AddField(
            model_name='invoice',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.product'),
        ),
    ]

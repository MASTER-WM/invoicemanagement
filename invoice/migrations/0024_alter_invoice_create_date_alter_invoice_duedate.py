# Generated by Django 4.0.1 on 2022-01-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0023_alter_invoice_create_date_alter_invoice_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='create_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='dueDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
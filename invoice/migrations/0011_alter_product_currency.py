# Generated by Django 4.0.1 on 2022-01-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_alter_invoice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('ریال', 'ریال'), ('دلار', 'دلار')], default='ریال', max_length=100),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_alter_product_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='create_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0009_supplier_description_supplier_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='suppliers',
        ),
    ]
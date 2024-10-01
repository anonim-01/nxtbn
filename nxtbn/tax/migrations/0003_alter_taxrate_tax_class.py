# Generated by Django 4.2.11 on 2024-10-01 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0002_remove_taxrate_exempt_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxrate',
            name='tax_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tax_rates', to='tax.taxclass'),
        ),
    ]
